import LateralMenu from '@/components/navbars/LateralMenu'
import { Tag } from '@/lib/types/others';
import { Factory, Video } from 'lucide-react';
import { Outlet } from 'react-router-dom';

const tags: Tag[] = [
    {name: "Cámara",path: "/registers/create",icon: <Video className='w-4'/>},
    {name: "Registros",path: "/registers",icon: <Factory className='w-4'/>}
];

export default function Attendance() {
    return (
        <section className='gap-6 flex flex-row mt-5'>
            <LateralMenu key={1} tags={tags}/>
            <div className='w-full pb-30'>
                <Outlet/>
            </div>
        </section>
    )
}