import LateralMenu from '@/components/navbars/LateralMenu'
import { Tag } from '@/lib/types/others';
import { Factory, Grip } from 'lucide-react';
import { Outlet } from 'react-router-dom';

const tags: Tag[] = [
    {name: "Departamentos",path: "/settings/departments",icon: <Factory className='w-4'/>},
    {name: "Cargos",path: "/settings/positions",icon: <Grip className='w-4'/>},
];
function Setting() {
    return (
        <section className='gap-6 flex flex-row mt-5'>
            <LateralMenu key={1} tags={tags}/>
            <div className='w-full pb-30'>
                <Outlet/>
            </div>
        </section>
    )
}

export default Setting
