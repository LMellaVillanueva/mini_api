import { useContext } from 'react'
import { UsersContext } from '../context/UserContext'

const Users = () => {
  const { users, setCategory, category } = useContext(UsersContext)

  

  return (
    <main className="p-4">
      <h1 className="text-2xl font-bold mb-4">User's List</h1>
      <div className="flex gap-2 mb-6">
        <button 
          onClick={() => setCategory('users')} 
          className={`px-4 py-2 rounded border ${category === 'users' ? 'bg-blue-600 text-white' : 'bg-white text-black'}`}
        >
          All Users
        </button>
        <button 
          onClick={() => setCategory('all_actives')} 
          className={`px-4 py-2 rounded border ${category === 'all_actives' ? 'bg-blue-600 text-white' : 'bg-white text-black'}`}
        >
          Actives
        </button>
        <button 
          onClick={() => setCategory('all_inactives')} 
          className={`px-4 py-2 rounded border ${category === 'all_inactives' ? 'bg-blue-600 text-white' : 'bg-white text-black'}`}
        >
          Inactives
        </button>
        <button 
          onClick={() => setCategory('email')} 
          className={`px-4 py-2 rounded border ${category === 'email' ? 'bg-blue-600 text-white' : 'bg-white text-black'}`}
        >
          Valid Emails
        </button>
        <button 
          onClick={() => setCategory('mean')} 
          className={`px-4 py-2 rounded border ${category === 'mean' ? 'bg-blue-600 text-white' : 'bg-white text-black'}`}
        >
          Mean
        </button>
        <button 
          onClick={() => setCategory('max_age')} 
          className={`px-4 py-2 rounded border ${category === 'max_age' ? 'bg-blue-600 text-white' : 'bg-white text-black'}`}
        >
          Max Age
        </button>
        <button 
          onClick={() => setCategory('min_age')} 
          className={`px-4 py-2 rounded border ${category === 'min_age' ? 'bg-blue-600 text-white' : 'bg-white text-black'}`}
        >
          Min Age
        </button>
      </div>
      <table className="border border-gray-300 border-collapse w-full">
        <thead>
          <tr className="">
            <th className="border border-gray-300 px-4 py-2 text-left">ID</th>
            <th className="border border-gray-300 px-4 py-2 text-left">Name</th>
            <th className="border border-gray-300 px-4 py-2 text-left">Email</th>
            <th className="border border-gray-300 px-4 py-2 text-left">Age</th>
            <th className="border border-gray-300 px-4 py-2 text-left">Status</th>
          </tr>
        </thead>
        <tbody>
          {users && users.length > 0 ? (
            users.map((user) => (
              <tr key={user.id} className="">
                <td className="border border-gray-300 px-4 py-2">{user.id}</td>
                <td className="border border-gray-300 px-4 py-2">{user.name}</td>
                <td className="border border-gray-300 px-4 py-2">{user.email}</td>
                <td className="border border-gray-300 px-4 py-2">{user.age}</td>
                <td className="border border-gray-300 px-4 py-2">
                  <span className={`px-2 py-1 rounded text-xs ${user.active ? 'bg-green-200 text-green-800' : 'bg-red-200 text-red-800'}`}>
                    {user.active ? 'Active' : 'Inactive'}
                  </span>
                </td>
              </tr>
            ))
          ) : (
            <tr>
              <td colSpan="5" className="text-center py-4 text-gray-500">
                No users found or loading data...
              </td>
            </tr>
          )}
        </tbody>
      </table>
    </main>
  )
}

export default Users