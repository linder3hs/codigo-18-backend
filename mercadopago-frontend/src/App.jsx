import { initMercadoPago, Wallet } from "@mercadopago/sdk-react";

initMercadoPago("...");

export default function App() {
  return (
    <main className="max-w-lg m-auto">
      <section className="p-6">
        <h1 className="text-center text-2xl font-bold">
          Integrando Mercado Pago
        </h1>
        <Wallet
          initialization={{
            preferenceId: "1605982166-c495d7ee-dc51-4651-93c2-9d9608dcf7b7",
          }}
        />
      </section>
    </main>
  );
}
