import { useEffect } from 'react'
import { navigate } from '../lib/router'

/** The old guest sign-up form is gone: signing in (Google) is also how a parent signs up. Old links land on the sign-in page. */
export default function Start() {
  useEffect(() => { navigate('/signin') }, [])
  return null
}
