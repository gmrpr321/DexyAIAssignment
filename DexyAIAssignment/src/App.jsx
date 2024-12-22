import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import Header from '../components/Header/Header'
import Styles from './App.module.css'
import MessageForm from '../components/MessageForm/MessageForrm'
function App() {
  const [count, setCount] = useState(0)

  return (
    <>
     <div className={Styles.background}>
      <Header></Header>
      <div className={Styles.body}>
        <MessageForm></MessageForm>

        </div>
     </div>
    </>
  )
}

export default App
