import './App.css'
import Users from './components/Users'

function App() {

  return (
    <main className='flex flex-col gap-16'>
      <header>
        <h1>Welcome to Mini Users Manager</h1>
      </header>
      <Users/>
    </main>
  )
}

export default App
