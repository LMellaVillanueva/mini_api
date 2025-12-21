import { createContext, useEffect, useState } from 'react'

export const UsersContext = createContext()

export const UsersProvider = ({ children }) => {

  const [users, setUsers] = useState([])
  const [category, setCategory] = useState('users')

  useEffect(() => {
    const fetchUsers = async () => {
        try {
            const response = await fetch(`http://127.0.0.1:5000/users/stats/${category}`)
            if (response.ok) {
              const data = await response.json()
              setUsers(data.users)
            }
          } catch (error) {
            console.log(`Error al llamar a la API: ${error}`)
        }
    }
    fetchUsers()
  }, [category])

  return (
    <UsersContext.Provider value={{ users, setCategory, category }}>
        {children}
    </UsersContext.Provider>
  )
}
