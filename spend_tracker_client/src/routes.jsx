import Dashboard from "./pages/Dashboard";
import UploadStatements from "./pages/UploadStatements";
import Transactions from "./pages/Transactions";
import Insights from "./pages/Insights";
import ManualExpense from "./pages/ManualExpense";

export const routes = [
  { path: "/", element: <Dashboard /> },
  { path: "/upload", element: <UploadStatements /> },
  { path: "/transactions", element: <Transactions /> },
  { path: "/insights", element: <Insights /> },
  { path: "/manual-expense", element: <ManualExpense /> },
];