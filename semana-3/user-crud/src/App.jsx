import { useState } from "react";
import "./App.css";

function App() {
  const [users, setUsers] = useState([]);

  const getUsers = async () => {
    const response = await fetch("http://127.0.0.1:7000/api/v1/user");
    const data = await response.json();
    setUsers(data.users);
  };

  return (
    <>
      <main className="main-container">
        <section>
          <h1>Listar usuarios</h1>
          <div>
            <button onClick={getUsers}>Obtener usuarios</button>
          </div>
          <div>
            <div
              style={{
                display: "flex",
                flexDirection: "column",
                gap: 20,
                marginTop: 40,
              }}
            >
              {users.map((user) => (
                <div key={user.id} className="card">
                  <h4>{user.full_name}</h4>
                  <p>{user.email}</p>
                </div>
              ))}
            </div>
          </div>
        </section>
        <section>
          <h2>Crear Ususarios</h2>
        </section>
      </main>
    </>
  );
}

export default App;
