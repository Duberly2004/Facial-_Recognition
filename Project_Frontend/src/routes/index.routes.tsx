import { useRoutes } from "react-router-dom";

import appRouter from "@/routes/app.routes";

function AppRouter() {
  return useRoutes([...appRouter]);
}

export default AppRouter;