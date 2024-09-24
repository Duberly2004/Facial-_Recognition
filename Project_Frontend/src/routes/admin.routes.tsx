import Base from "@/modules/base/Base";
import { Student } from "@/modules/students/Student";
import { Teacher } from "@/modules/teachers/Teacher";
import Settings from "@/pages/Settings";
import { RouteObject } from "react-router-dom";

export const admin_routes:RouteObject[] = [
    {path:"teachers",element:<Teacher/>},
    {path:"students",element:<Student/>},
    {path:"settings",element:<Settings/>,children:[
        {path:"",element:<Base endpointName="admin/courses"/>},
        {path:"cycles",element:<Base endpointName="admin/cycles"/>},
        {path:"sections",element:<Base endpointName="admin/sections"/>},
        {path:"careers",element:<Base endpointName="admin/careers"/>}
    ]},

]

export default admin_routes