import AppLayout from "@/layouts/AppLayout";
import AttendaceList from "@/modules/Attendance/AttendaceList";
import Attendance from "@/modules/Attendance/Attendance";
import AttendanceCreate from "@/modules/Attendance/AttendanceCreate";
import Student from "@/modules/student/Student";
import Setting from "@/pages/Setting";
const appRouter = [
  {
    path: "/",
    element: <AppLayout />,
    children: [
      {
        path: "attendances",
        element: <Attendance />,
        children:[
          {
            path: "",
            element: <AttendaceList/>,
          },
          {
            path: "/attendances/create",
            element: <AttendanceCreate/>,
          },
        ]
      },
      {
        path: "/students",
        element: <Student />,
      },
      {
        path: "/settings",
        element: <Setting />,
      },
    ]
}]
export default appRouter