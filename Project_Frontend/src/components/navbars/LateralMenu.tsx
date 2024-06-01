import { Tag } from "@/lib/types/others"
import { useLocation, useNavigate } from "react-router-dom"
interface Props{
    tags:Tag[]
}

export default function LateralMenu({tags}:Props) {
  const navigateTo = useNavigate()
  const location = useLocation()

  return (
      <div className="w-48">
        {tags.map((tag,index) => (
          <div onClick={()=>navigateTo(tag.path.toString())} key={index} className={`${location.pathname===tag.path? "bg-primary hover:bg-none text-white":""} dark:hover:bg-sky-950 hover:bg-primary hover:text-white`}>
            <hr className="my-2" />
            <div key={index} className="px-2 flex gap-1 items-center text-sm cursor-pointer">
            {tag.icon}{tag.name}
            </div>
            <hr className="my-2" />
          </div>
        ))}
      </div>
  )
}