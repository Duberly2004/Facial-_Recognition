import React from "react";
import {
  Tooltip,
  TooltipContent,
  TooltipProvider,
  TooltipTrigger,
} from "../ui/tooltip";
import { Button } from "../ui/button";
import { ArrowRightLeft, FilePlus2, Settings, Users } from "lucide-react";
import { NavLink, useLocation } from "react-router-dom";

interface Item {
  name: string
  url: string
  icon: React.ReactNode
}
const items: Item[] = [
  {
    name: "Registros",
    url: "/registers",
    icon: <FilePlus2 />,
  },
  {
    name: "Usuarios",
    url: "/users",
    icon: <Users />,
  },
]

interface NavbarProps {
  isExpanded: boolean;
  btnUpdateMenuVisibility: () => void;
}
export function AppNavbar({ isExpanded, btnUpdateMenuVisibility }: NavbarProps) {
  return (
    <nav className="pt-6 h-screen overflow-y-auto pb-60">
      <div className="relative">
        {items.map((data, index) => (
          <SidebarItem key={index} {...data} isExpanded={isExpanded} />
        ))}
        <SidebarItem name="Configuración" url="/settings/departments" icon={<Settings />} isExpanded={isExpanded} /> 
      </div>
      <TooltipProvider delayDuration={10}>
        <Tooltip>
          <TooltipTrigger
            asChild
            onClick={btnUpdateMenuVisibility}
            className="z-50 absolute top-[20rem] xl:top-[20rem] h-10 -right-[2.5rem]"
          >
            <Button className="z-50">
              <ArrowRightLeft className="w-4" />
            </Button>
          </TooltipTrigger>
          <TooltipContent>
            {isExpanded ? <span>Cerrar</span> : <span>Abrir</span>}
          </TooltipContent>
        </Tooltip>
      </TooltipProvider>
    </nav>
  );
}

interface Props {
  name?: string;
  url: string;
  icon: any;
  isExpanded: boolean;
}

export function SidebarItem({ name, url, icon, isExpanded }: Props) {
  const location = useLocation();
  const is_active = location.pathname.split("/")[1] === url.split("/")[1];
  return (
    <NavLink
      to={url}
      className={`group flex relative ${isExpanded
        ? "w-[12rem] ml-4 origin-left transition-all duration-75"
        : "w-[2.6rem]"
        } h-[3.8rem] mx-auto`}
    >
      <div
        className={`${is_active && "bg-primary group-active:text-white dark:text-black"
          } p-2 w-full group-hover:bg-primary group-hover:text-white dark:group-hover:text-black rounded transition-all duration-75 origin-left mt-5 flex gap-5 ${is_active &&
          isExpanded &&
          "bg-primary origin-left text-white dark:text-black"
          }`}
      >
        <span className={`text-primary group-hover:text-white ${is_active && 'text-white'}`}>{icon}</span>
        <span className={`${!isExpanded && "scale-0"} origin-left`}>
          {name}
        </span>
      </div>
    </NavLink>
  );
}