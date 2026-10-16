// Single place that touches import.meta.env (keeps everything else framework-agnostic).
export const API_MODE: 'mock' | 'live' =
  ((import.meta as any).env?.VITE_API_MODE as 'mock' | 'live') || 'mock'
