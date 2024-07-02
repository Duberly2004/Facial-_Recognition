import AppLayout from "@/layouts/AppLayout";
import AttendaceList from "@/modules/Attendance/AttendaceList";
import Attendance from "@/modules/Attendance/Attendance";
import AttendanceCreate from "@/modules/Attendance/AttendanceCreate";
import Department from "@/modules/admin/Department";
import Position from "@/modules/admin/Position";
import User from "@/modules/user/User";
import Setting from "@/pages/Setting";
const appRouter = [
  {
    path: "/",
    element: <AppLayout />,
    children: [
      {
        path: "registers",
        element: <Attendance />,
        children:[
          {
            path: "",
            element: <AttendaceList/>,
          },
          {
            path: "/registers/create",
            element: <AttendanceCreate/>,
          },
        ]
      },
      {
        path: "/users",
        element: <User />,
      },
      {
        path: "/settings",
        element: <Setting />,
        children:[
          {
            path: "/settings/departments",
            element: <Department/>,
          },
          {
            path: "/settings/positions",
            element: <Position/>,
          },
        ]
      },
    ]
}]
export default appRouter