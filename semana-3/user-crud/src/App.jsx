import { useState } from "react";
import "./App.css";

function App() {
  const [users, setUsers] = useState([]);

  const getUsers = async () => {
    const response = await fetch("http://127.0.0.1:7000/api/v1/user");
    const data = await response.json();
    console.log(data);
  };

  return (
    <>
      <main className="main-container">
        <section>
          <h1>Listar usuarios</h1>
          <div>
            <button onClick={getUsers}>Obtener usuarios</button>
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
