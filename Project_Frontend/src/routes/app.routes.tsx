import AppLayout from "@/layouts/AppLayout";
import Login from "@/pages/Login";
import { RouteObject } from "react-router-dom";
import admin_routes from "./admin.routes";
import { teacher_routes } from "./teacher.routes";

const appRouter:RouteObject[] = [
  {
    path: "/",
    element: <Login/>,
  },
  {
    path:"/admin",
    element:<AppLayout/>,
    children: admin_routes
  },
  {
    path:"/teacher",
    element:<AppLayout/>,
    children: teacher_routes
  }
]
export default appRouter