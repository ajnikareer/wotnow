import { createContext, useCallback, useContext, useRef, useState, type ReactNode } from 'react'
import { Toast } from '../components/ui'

const Ctx = createContext<(t: string) => void>(() => {})
export function ToastProvider({ children }: { children: ReactNode }) {
  const [text, setText] = useState<string | null>(null)
  const timer = useRef<ReturnType<typeof setTimeout>>()
  const show = useCallback((t: string) => {
    setText(t); clearTimeout(timer.current); timer.current = setTimeout(() => setText(null), 2400)
  }, [])
  return <Ctx.Provider value={show}>{children}<Toast text={text} /></Ctx.Provider>
}
export const useToast = () => useContext(Ctx)
