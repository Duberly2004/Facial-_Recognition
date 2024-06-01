import {
    Avatar,
    AvatarFallback,
    AvatarImage,
} from "@/components/ui/avatar"
interface Props {
    src:string
    name:string
}
export function UserAvatar(props:Props) {
    return (
        <Avatar>
            <AvatarImage src={props.src} alt={'Avatar '+props.name} />
            <AvatarFallback>{props.name}</AvatarFallback>
        </Avatar>
    )
}