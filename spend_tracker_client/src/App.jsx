import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import { routes } from "./routes";

function App() {
  return (
    <BrowserRouter>
      <div style={{ padding: "20px" }}>
        <h1>Spend Tracker</h1>

        <nav style={{ display: "flex", gap: "12px", marginBottom: "20px" }}>
          <Link to="/">Dashboard</Link>
          <Link to="/upload">Upload</Link>
          <Link to="/transactions">Transactions</Link>
          <Link to="/manual-expense">Manual Expense</Link>
          <Link to="/insights">Insights</Link>
        </nav>

        <Routes>
          {routes.map((route) => (
            <Route key={route.path} path={route.path} element={route.element} />
          ))}
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;