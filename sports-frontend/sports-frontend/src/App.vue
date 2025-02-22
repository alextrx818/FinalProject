<template>
  <div class="q-pa-md">
    <q-card class="my-card">
      <q-card-section>
        <div class="text-h6">Tennis Match Data</div>
        <div class="text-subtitle2">
          Status: {{ connectionStatus }}
          <span v-if="lastMessageTime">(Last update: {{ lastMessageTime }})</span>
        </div>
      </q-card-section>
      
      <q-card-section>
        <div v-if="sortedMatches.length === 0" class="text-center q-pa-md">
          <q-spinner color="primary" size="2em" />
          <p>Waiting for match data...</p>
        </div>
        
        <div v-else v-for="match in sortedMatches" :key="match.home_player + match.away_player" class="match-card">
          <div class="match-header">
            <h3>{{ match.home_player }} vs {{ match.away_player }}</h3>
            <span class="status">{{ match.status }}</span>
          </div>
          <div class="odds-container">
            <div class="odds-section">
              <h4>Pre-match Odds</h4>
              <p>{{ match.pre_match_odds || 'N/A' }}</p>
            </div>
            <div class="odds-section">
              <h4>Live Odds</h4>
              <p>{{ match.live_odds || 'N/A' }}</p>
            </div>
          </div>
          <div class="last-updated">
            Updated: {{ new Date(match.lastUpdated).toLocaleTimeString() }}
          </div>
        </div>
      </q-card-section>
    </q-card>
  </div>
</template>

<script>
export default {
  data() {
    return {
      matches: {},  // Object to track matches by ID
      ws: null,
      lastMessageTime: null,
      connectionStatus: 'Disconnected',
      reconnectAttempts: 0,
      maxReconnectAttempts: 5,
      reconnectDelay: 1000 // Start with 1 second delay
    }
  },
  computed: {
    sortedMatches() {
      // Convert matches object to array and sort by player names
      return Object.values(this.matches).sort((a, b) => {
        return `${a.home_player} ${a.away_player}`.localeCompare(`${b.home_player} ${b.away_player}`)
      })
    }
  },
  methods: {
    connectWebSocket() {
      if (this.ws?.readyState === WebSocket.OPEN) {
        console.log('WebSocket already connected')
        return
      }

      try {
        this.ws = new WebSocket('wss://livesportsalerts.io/ws')
        this.connectionStatus = 'Connecting...'
        
        this.ws.onopen = () => {
          console.log('WebSocket connected')
          this.connectionStatus = 'Connected'
          this.reconnectAttempts = 0
          this.reconnectDelay = 1000
        }
        
        this.ws.onmessage = (event) => {
          try {
            const data = JSON.parse(event.data)
            console.log('Received data:', data)
            
            if (!Array.isArray(data)) {
              console.warn('Received non-array data:', data)
              return
            }
            
            // Update matches object with new data
            data.forEach(match => {
              if (!match.home_player || !match.away_player) {
                console.warn('Invalid match data:', match)
                return
              }
              
              // Create a unique ID from player names
              const matchId = `${match.home_player}-${match.away_player}`
              
              // Update existing match or add new one
              this.$set(this.matches, matchId, {
                ...this.matches[matchId],  // Keep existing data
                ...match,  // Update with new data
                lastUpdated: new Date().toISOString()
              })
            })
            
            this.lastMessageTime = new Date().toLocaleTimeString()
          } catch (error) {
            console.error('Error parsing WebSocket data:', error)
          }
        }
        
        this.ws.onclose = (event) => {
          console.log('WebSocket disconnected:', event)
          this.connectionStatus = 'Disconnected'
          this.ws = null
          
          // Implement exponential backoff for reconnection
          if (this.reconnectAttempts < this.maxReconnectAttempts) {
            const delay = Math.min(1000 * Math.pow(2, this.reconnectAttempts), 30000)
            console.log(`Reconnecting in ${delay}ms (attempt ${this.reconnectAttempts + 1})`)
            setTimeout(() => {
              this.reconnectAttempts++
              this.connectWebSocket()
            }, delay)
          } else {
            this.connectionStatus = 'Failed to connect'
            console.error('Max reconnection attempts reached')
          }
        }
        
        this.ws.onerror = (error) => {
          console.error('WebSocket error:', error)
          this.connectionStatus = 'Error'
        }
      } catch (error) {
        console.error('Error creating WebSocket:', error)
        this.connectionStatus = 'Error'
      }
    },
    
    cleanupWebSocket() {
      if (this.ws) {
        try {
          this.ws.close()
        } catch (error) {
          console.error('Error closing WebSocket:', error)
        }
        this.ws = null
      }
    }
  },
  mounted() {
    this.connectWebSocket()
    
    // Add window visibility change handler
    document.addEventListener('visibilitychange', () => {
      if (document.visibilityState === 'visible') {
        // Page is visible again, check connection
        if (!this.ws || this.ws.readyState !== WebSocket.OPEN) {
          console.log('Page visible, reconnecting WebSocket')
          this.connectWebSocket()
        }
      }
    })
  },
  beforeUnmount() {
    this.cleanupWebSocket()
    document.removeEventListener('visibilitychange')
  }
}
</script>

<style scoped>
.match-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  padding: 16px;
  margin-bottom: 16px;
  background: white;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.match-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 12px;
}

.match-header h3 {
  margin: 0;
  font-size: 1.2em;
}

.status {
  padding: 4px 8px;
  border-radius: 4px;
  background: #f0f0f0;
  font-size: 0.9em;
}

.odds-container {
  display: flex;
  gap: 16px;
  margin-bottom: 8px;
}

.odds-section {
  flex: 1;
  padding: 8px;
  background: #f8f8f8;
  border-radius: 4px;
}

.odds-section h4 {
  margin: 0 0 8px 0;
  font-size: 1em;
  color: #666;
}

.odds-section p {
  margin: 0;
  font-size: 1.2em;
  font-weight: bold;
}

.last-updated {
  font-size: 0.8em;
  color: #666;
  text-align: right;
}
</style>
