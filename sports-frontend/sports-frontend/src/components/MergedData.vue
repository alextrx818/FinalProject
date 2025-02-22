<template>
  <div>
    <h1>Raw Merged Tennis Data</h1>
    <div v-if="loading">Loading...</div>
    <div v-else-if="error" class="error">Error: {{ error }}</div>
    <pre v-else>{{ mergedData || 'No data available' }}</pre>
  </div>
</template>

<script>
export default {
  name: "MergedData",
  data() {
    return {
      mergedData: null,
      loading: false,
      error: null
    };
  },
  methods: {
    async fetchData() {
      this.loading = true;
      this.error = null;
      try {
        const response = await fetch("http://localhost:8000/merged_data");
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        console.log('Fetched data:', data);  // Debug log
        this.mergedData = data;
      } catch (error) {
        console.error("Error fetching merged data:", error);
        this.error = error.message;
      } finally {
        this.loading = false;
      }
    }
  },
  mounted() {
    this.fetchData();
    // Refresh data every 30 seconds
    setInterval(this.fetchData, 30000);
  }
};
</script>

<style scoped>
pre {
  background-color: #f5f5f5;
  padding: 1rem;
  border-radius: 4px;
  overflow-x: auto;
  white-space: pre-wrap;
  word-wrap: break-word;
}

h1 {
  color: #2c3e50;
  margin-bottom: 1rem;
}

.error {
  color: red;
  margin: 1rem 0;
}
</style>
