<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="bg-primary text-white">
      <q-toolbar>
        <q-toolbar-title>
          Sports Odds Dashboard (Live Updates)
        </q-toolbar-title>
      </q-toolbar>
    </q-header>

    <q-page-container>
      <q-page padding>
        <div class="row q-col-gutter-md q-mb-md">
          <div class="col-12 col-md-4">
            <q-card class="bg-positive text-white">
              <q-card-section>
                <div class="text-h6">Active Matches</div>
                <div class="text-h4">{{ activeLiveMatches }}</div>
              </q-card-section>
            </q-card>
          </div>
          <div class="col-12 col-md-4">
            <q-card class="bg-info text-white">
              <q-card-section>
                <div class="text-h6">Total Events</div>
                <div class="text-h4">{{ events.length }}</div>
              </q-card-section>
            </q-card>
          </div>
          <div class="col-12 col-md-4">
            <q-card class="bg-warning text-white">
              <q-card-section>
                <div class="text-h6">Last Update</div>
                <div class="text-subtitle1">{{ lastUpdateTime }}</div>
              </q-card-section>
            </q-card>
          </div>
        </div>

        <q-card>
          <q-card-section class="row items-center">
            <div class="text-h6">Live Sports Odds</div>
            <q-space />
            <q-spinner v-if="loading" color="primary" size="2em" />
          </q-card-section>
          
          <q-card-section>
            <q-table
              :rows="events"
              :columns="columns"
              row-key="id"
              :rows-per-page-options="[10, 20, 50]"
              flat
              bordered
            >
              <template v-slot:body-cell-status="props">
                <q-td :props="props">
                  <q-chip :color="props.row.status === 'Live' ? 'positive' : 'grey'" text-color="white" size="sm">
                    {{ props.row.status }}
                  </q-chip>
                </q-td>
              </template>
              <template v-slot:body-cell-trend="props">
                <q-td :props="props">
                  <q-icon 
                    v-if="props.row.trend !== 0"
                    :name="props.row.trend > 0 ? 'arrow_upward' : 'arrow_downward'" 
                    :color="props.row.trend > 0 ? 'positive' : 'negative'"
                  />
                  {{ Math.abs(props.row.trend).toFixed(2) }}
                </q-td>
              </template>
            </q-table>
          </q-card-section>
        </q-card>

        <q-card class="q-ma-md">
          <q-table
            title="Karina's Last 10 Games"
            :rows="karinaGames"
            :columns="karinaColumns"
            :pagination="{ rowsPerPage: 10 }"
            virtual-scroll
            style="height: 300px"
            row-key="date"
          />
        </q-card>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  name: "App",
  data() {
    return {
      columns: [
        { name: "match_name", label: "Match", field: "match_name", align: 'left' },
        { name: "sport", label: "Sport", field: "sport", align: 'left' },
        { name: "status", label: "Status", field: "status", align: 'left' },
        { name: "pre_odds", label: "Pre-match Odds", field: "pre_odds", align: 'right' },
        { name: "live_odds", label: "Live Odds", field: "live_odds", align: 'right' },
        { name: "trend", label: "Trend", field: "trend", align: 'right' }
      ],
      events: [],
      loading: false,
      lastUpdateTime: '-',
      karinaColumns: [
        { name: 'date', label: 'Date', align: 'left' },
        { name: 'opponent', label: 'Opponent', align: 'left' },
        { name: 'result', label: 'Result', align: 'left' }
      ],
      karinaGames: [
        { date: '2025-02-15', opponent: 'Smith', result: 'Win' },
        { date: '2025-02-14', opponent: 'Johnson', result: 'Loss' },
        { date: '2025-02-13', opponent: 'Williams', result: 'Win' },
        { date: '2025-02-12', opponent: 'Brown', result: 'Win' },
        { date: '2025-02-11', opponent: 'Davis', result: 'Loss' },
        { date: '2025-02-10', opponent: 'Miller', result: 'Win' },
        { date: '2025-02-09', opponent: 'Wilson', result: 'Win' },
        { date: '2025-02-08', opponent: 'Moore', result: 'Loss' },
        { date: '2025-02-07', opponent: 'Taylor', result: 'Win' },
        { date: '2025-02-06', opponent: 'Anderson', result: 'Win' }
      ]
    }
  },
  computed: {
    activeLiveMatches() {
      return this.events.filter(event => event.status === 'Live').length
    }
  },
  mounted() {
    this.fetchOdds()
    setInterval(() => this.fetchOdds(), 60000) // 60 seconds
  },
  methods: {
    async fetchOdds() {
      this.loading = true
      try {
        const res = await fetch('http://localhost:5000/api/odds/live')
        const response = await res.json()
        this.events = response.data
        this.lastUpdateTime = new Date().toLocaleTimeString()
      } catch (err) {
        console.error('Error fetching odds:', err)
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style>
.q-table__card {
  box-shadow: 0 1px 5px rgba(0, 0, 0, 0.2);
}
</style>
