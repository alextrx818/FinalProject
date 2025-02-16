import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'
import { quasar, transformAssetUrls } from '@quasar/vite-plugin'

export default defineConfig({
  plugins: [
    vue({
      template: { transformAssetUrls }
    }),
    quasar()
  ],
  server: {
    host: '0.0.0.0', // Listen on all addresses
    port: 5173,
    strictPort: true, // Fail if port is already in use
    hmr: {
      clientPort: 5173 // Force the HMR client to use this port
    }
  }
})
