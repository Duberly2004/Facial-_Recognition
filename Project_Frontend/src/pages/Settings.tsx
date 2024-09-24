import LateralMenu from '@/components/navbars/LateralMenu'
import { Tag } from '@/lib/types/others';
import { BookOpen, CreditCard, Factory, Grip } from 'lucide-react';
import { Outlet } from 'react-router-dom';

const tags: Tag[] = [
    {name: "Cursos",path: "/admin/settings",icon: <BookOpen className='w-4'/>},
    {name: "Carreras",path: "/admin/settings/careers",icon: <CreditCard className='w-4'/>},
    {name: "Secciones",path: "/admin/settings/sections",icon: <Grip className='w-4'/>},
    {name: "Ciclos",path: "/admin/settings/Cycles",icon: <Factory className='w-4'/>},
];
function Settings() {
    return (
        <section className='gap-6 flex flex-row mt-5'>
            <LateralMenu key={1} tags={tags}/>
            <div className='w-full pb-30'>
                <Outlet/>
            </div>
        </section>
    )
}

export default Settings
