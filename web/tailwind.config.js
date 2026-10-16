/** Colours come from CSS variables (src/index.css) so light/dark switch instantly. */
const v = (name) => `rgb(var(--${name}) / <alpha-value>)`
export default {
  darkMode: 'class',
  content: ['./index.html', './src/**/*.{ts,tsx}'],
  theme: {
    extend: {
      colors: {
        bg: v('bg'), surface: v('surface'), surface2: v('surface2'), surface3: v('surface3'),
        line: v('line'), ink: v('ink'), muted: v('muted'), faint: v('faint'),
        brand: { violet: '#8B5CF6', cyan: '#22D3EE', mint: '#34D399' },
        ok: '#10B981', bad: '#EF4444', warn: '#F59E0B',
      },
      fontFamily: {
        sans: ['"Plus Jakarta Sans Variable"', '"Plus Jakarta Sans"', 'system-ui', '-apple-system', '"Segoe UI"', 'Roboto', 'sans-serif'],
        display: ['"Bricolage Grotesque Variable"', '"Bricolage Grotesque"', '"Plus Jakarta Sans Variable"', 'system-ui', '"Segoe UI"', 'sans-serif'],
      },
      borderRadius: { '4xl': '2rem' },
      boxShadow: {
        soft: '0 1px 2px rgb(0 0 0 / .04), 0 8px 24px -12px rgb(0 0 0 / .12)',
        glow: '0 10px 30px -8px rgb(139 92 246 / .45)',
      },
      keyframes: {
        blink: { '0%,92%,100%': { transform: 'scaleY(1)' }, '95%': { transform: 'scaleY(.1)' } },
        wander: { '0%,100%': { transform: 'translate(0,0)' }, '30%': { transform: 'translate(3px,-4px)' }, '60%': { transform: 'translate(-3px,-2px)' } },
        bob: { '0%,100%': { transform: 'translateY(0)' }, '50%': { transform: 'translateY(-6px)' } },
        pop: { '0%': { transform: 'scale(.6)', opacity: 0 }, '70%': { transform: 'scale(1.06)', opacity: 1 }, '100%': { transform: 'scale(1)' } },
        rise: { '0%': { transform: 'translateY(10px)', opacity: 0 }, '100%': { transform: 'translateY(0)', opacity: 1 } },
        shake: { '0%,100%': { transform: 'translateX(0)' }, '25%': { transform: 'translateX(-4px)' }, '75%': { transform: 'translateX(4px)' } },
      },
      animation: {
        blink: 'blink 4s infinite', wander: 'wander 2.4s ease-in-out infinite', bob: 'bob 3s ease-in-out infinite',
        pop: 'pop .45s cubic-bezier(.2,.9,.3,1.2) both', rise: 'rise .4s ease-out both', shake: 'shake .35s ease-in-out 2',
      },
    },
  },
  plugins: [],
}
