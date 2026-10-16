import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

// During development, /api is proxied to the backend (FastAPI on :8080) when VITE_API_MODE=live.
export default defineConfig({
  plugins: [react()],
  server: { port: 5173, proxy: { '/api': 'http://localhost:8080' } },
})
