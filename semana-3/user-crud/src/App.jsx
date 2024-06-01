import { useState } from "react";
import "./App.css";

function App() {
  const [users, setUsers] = useState([]);

  const [inputValues, setInputValues] = useState({
    name: "",
    lastname: "",
    email: "",
    password: "",
    phone_number: "",
    genre: "",
  });

  const handleInputChange = (event) => {
    setInputValues({
      ...inputValues,
      [event.target.name]: event.target.value,
    });
  };

  const handleForm = async (event) => {
    event.preventDefault();
    const response = await fetch("http://127.0.0.1:7000/api/v1/user", {
      method: "POST",
      body: JSON.stringify(inputValues),
      headers: {
        "Content-type": "application/json",
      },
    });
    const data = await response.json();
    console.log(data);
  };

  const getUsers = async () => {
    const response = await fetch("http://127.0.0.1:7000/api/v1/user");
    const data = await response.json();
    setUsers(data.users);
  };

  const deleteUser = async (user_id) => {
    const response = await fetch(
      `http://127.0.0.1:7000/api/v1/user/${user_id}`,
      {
        method: "DELETE",
        headers: {
          "Content-type": "application/json",
        },
      }
    );
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
                  <button
                    onClick={() => deleteUser(user.id)}
                    style={{
                      background: "red",
                    }}
                  >
                    Eliminar
                  </button>
                </div>
              ))}
            </div>
          </div>
        </section>
        <section>
          <h2>Crear Ususarios</h2>
          <div>
            <form action="" onSubmit={handleForm}>
              <div>
                <input
                  type="text"
                  name="name"
                  placeholder="Ingrese su nombre"
                  onChange={handleInputChange}
                  value={inputValues.name}
                />
              </div>
              <div>
                <input
                  type="text"
                  name="lastname"
                  placeholder="Ingrese su apellido"
                  onChange={handleInputChange}
                  value={inputValues.lastname}
                />
              </div>
              <div>
                <input
                  type="text"
                  name="phone_number"
                  placeholder="Ingrese su celular"
                  onChange={handleInputChange}
                  value={inputValues.phone_number}
                />
              </div>
              <div>
                <input
                  type="email"
                  name="email"
                  placeholder="Ingrese su email"
                  onChange={handleInputChange}
                  value={inputValues.email}
                />
              </div>
              <div>
                <input
                  type="password"
                  name="password"
                  placeholder="Ingrese su password"
                  onChange={handleInputChange}
                  value={inputValues.password}
                />
              </div>
              <div>
                <input
                  type="text"
                  name="genre"
                  placeholder="Ingrese su genero"
                  onChange={handleInputChange}
                  value={inputValues.genre}
                />
              </div>
              <div>
                <button>Crear usuario</button>
              </div>
            </form>
          </div>
        </section>
      </main>
    </>
  );
}

export default App;
