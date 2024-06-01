import { useState } from "react";
import { Link, Outlet } from "react-router-dom";
import { AppNavbar } from "@/components/navbars/AppNavbar";
import { Toaster } from "sonner";
import logo from "../assets/logo.jpeg"
function AppLayout() {
  const [isExpanded, setIsExpanded] = useState(false);

  const btnUpdateMenuVisibility = () => {
    setIsExpanded(!isExpanded);
  };

  return (
<div className="dark:bg-gray-950 w-full h-screen flex flex-col ">
      <div
        className=" w-[120rem] h-[100rem] rounded-full 
        fixed left-1/2 top-1/2 transform -translate-x-1/2 -translate-y-[125rem] "
      />
      <div className="bg-transparent h-[4.5rem] relative border-b-2 z-50 min-w-[590px]">
        <div
          className={` ${
            isExpanded ? "w-[15.4rem]" : "w-20"
          } duration-200 bg-background h-screen fixed top-0 border-r`}
        >
          <div className={`mx-auto pt-2 ${isExpanded && "pt-4"}`}>
            <Link to="/home" className="flex items-center">
              <img src={logo} className="ml-2 w-[3rem] h-16 origin-left duration-200 scale-100" />
            {isExpanded ? (
              <h1 className="text-4xl font-bold ml-1">G<span className="text-primary">9</span></h1>
              ) :null}
            </Link>
          </div>
          <div className="grow">
            <AppNavbar
              isExpanded={isExpanded}
              btnUpdateMenuVisibility={btnUpdateMenuVisibility}
            />
          </div>
        </div>
      </div>
      <div
        className={`transition-all duration-200 relative ml-10 xl:ml-0 px-20 xl:px-40 min-w-[550px]`}
      >
        <Outlet />
      </div>
      <Toaster richColors position="top-center"/>
    </div>
  );
}

export default AppLayout;