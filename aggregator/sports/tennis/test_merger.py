import unittest
from aggregator.sports.tennis.tennis_merger import TennisMerger

class TestTennisMerger(unittest.TestCase):
    def setUp(self):
        self.merger = TennisMerger()
        # Sample data from both APIs
        self.rapid_data = [
            {
                "raw_event_data": {
                    "home_player": "Francisco Comesana",
                    "away_player": "Gustavo Heide",
                    "score": "1-1"
                },
                "raw_odds_data": {
                    "Set 3 to Break Serve": {"Yes": 1.615, "No": 2.0}
                }
            },
            {
                "raw_event_data": {
                    "home_player": "N. Djokovic",
                    "away_player": "R. Nadal",
                    "score": "2-1"
                }
            }
        ]
        
        self.bets_data = [
            {
                "bet365_id": "169997177",
                "tournament": "Challenger Piracicaba",
                "players": {
                    "home": "Francisco Comesana",
                    "away": "Gustavo Heide"
                },
                "prematch_odds": {
                    "Match Winner": {
                        "Francisco Comesana": 1.85,
                        "Gustavo Heide": 1.95
                    }
                }
            },
            {
                "players": {
                    "home": "Novak Djokovic",
                    "away": "Rafael Nadal"
                }
            }
        ]

    def test_normalize_name(self):
        """Test name normalization"""
        test_cases = [
            ("N. Djokovic", "n djokovic"),
            ("Rafael Nadal", "rafael nadal"),
            ("F. Comesana", "f comesana"),
            ("", ""),
            ("J.R. Smith-Jones", "jr smith jones")
        ]
        for input_name, expected in test_cases:
            print(f"\nInput: {input_name}")
            result = self.merger.normalize_name(input_name)
            print(f"Result: {result}")
            print(f"Expected: {expected}")
            self.assertEqual(result, expected)

    def test_fuzzy_match_names(self):
        """Test fuzzy name matching"""
        matches = [
            ("N. Djokovic", "Novak Djokovic"),
            ("R. Nadal", "Rafael Nadal"),
            ("F. Comesana", "Francisco Comesana")
        ]
        non_matches = [
            ("N. Djokovic", "R. Nadal"),
            ("F. Comesana", "G. Heide")
        ]
        
        for name1, name2 in matches:
            self.assertTrue(self.merger.fuzzy_match_names(name1, name2))
        for name1, name2 in non_matches:
            self.assertFalse(self.merger.fuzzy_match_names(name1, name2))

    def test_names_are_equivalent(self):
        """Test player pairs matching"""
        # Direct match
        self.assertTrue(self.merger.names_are_equivalent(
            "Francisco Comesana", "Gustavo Heide",
            "Francisco Comesana", "Gustavo Heide"
        ))
        # Abbreviated match
        self.assertTrue(self.merger.names_are_equivalent(
            "N. Djokovic", "R. Nadal",
            "Novak Djokovic", "Rafael Nadal"
        ))
        # Non-match
        self.assertFalse(self.merger.names_are_equivalent(
            "Francisco Comesana", "Gustavo Heide",
            "Novak Djokovic", "Rafael Nadal"
        ))

    def test_merge_matching_records(self):
        """Test merging records that should match"""
        merged = self.merger.merge(self.bets_data, self.rapid_data)
        
        # Should find 2 matches (Comesana vs Heide and Djokovic vs Nadal)
        self.assertEqual(len(merged), 2)
        
        # Check first match (Comesana vs Heide)
        comesana_match = next(m for m in merged if "Comesana" in m["home_player"])
        self.assertIsNotNone(comesana_match["betsapi_data"])
        self.assertIsNotNone(comesana_match["rapid_data"])
        self.assertEqual(comesana_match["rapid_data"]["raw_event_data"]["score"], "1-1")
        
        # Check second match (Djokovic vs Nadal)
        djokovic_match = next(m for m in merged if "Djokovic" in m["home_player"])
        self.assertIsNotNone(djokovic_match["betsapi_data"])
        self.assertIsNotNone(djokovic_match["rapid_data"])
        self.assertEqual(djokovic_match["rapid_data"]["raw_event_data"]["score"], "2-1")

    def test_merge_unmatched_records(self):
        """Test handling of records that don't match between APIs"""
        # Add an extra record to rapid_data that won't match anything
        self.rapid_data.append({
            "raw_event_data": {
                "home_player": "Roger Federer",
                "away_player": "Andy Murray",
                "score": "3-3"
            }
        })
        
        merged = self.merger.merge(self.bets_data, self.rapid_data)
        
        # Should now have 3 records (2 matched + 1 unmatched)
        self.assertEqual(len(merged), 3)
        
        # Find the Federer match (should have rapid data but no bets data)
        federer_match = next(m for m in merged if "Federer" in m["home_player"])
        self.assertIsNone(federer_match["betsapi_data"])
        self.assertIsNotNone(federer_match["rapid_data"])
        self.assertEqual(federer_match["rapid_data"]["raw_event_data"]["score"], "3-3")

    def test_merge_events_and_odds(self):
        """Test merging events with their odds data"""
        # Convert rapid data to events and odds format
        events = []
        odds = {}
        
        for rd in self.rapid_data:
            event = {
                "match_id": rd.get("raw_event_data", {}).get("match_id", "169997177"),
                "home_player": rd.get("raw_event_data", {}).get("home_player"),
                "away_player": rd.get("raw_event_data", {}).get("away_player"),
                "score": rd.get("raw_event_data", {}).get("score"),
                "raw_odds_data": rd.get("raw_odds_data", {})  # Include raw odds data
            }
            events.append(event)
            odds[event["match_id"]] = rd.get("raw_odds_data", {})

        # Merge the data
        merged = self.merger.merge_events_and_odds(events, odds)
        
        # Verify the merge
        self.assertEqual(len(merged), 2)  # Should have two merged records
        
        comesana_match = next(m for m in merged if "Comesana" in m["home_player"])
        self.assertEqual(comesana_match["home_player"], "Francisco Comesana")
        self.assertEqual(comesana_match["away_player"], "Gustavo Heide")
        self.assertEqual(comesana_match["score"], "1-1")
        self.assertIn("Set 3 to Break Serve", comesana_match["odds"])
        
        djokovic_match = next(m for m in merged if "Djokovic" in m["home_player"])
        self.assertEqual(djokovic_match["home_player"], "N. Djokovic")
        self.assertEqual(djokovic_match["away_player"], "R. Nadal")
        self.assertEqual(djokovic_match["score"], "2-1")
        self.assertEqual(djokovic_match["odds"], {})

if __name__ == '__main__':
    unittest.main()
