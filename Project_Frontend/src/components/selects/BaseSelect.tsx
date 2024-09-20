import React from 'react';
import { useQuery } from 'react-query';
import { ILBase } from "@/lib/interfaces/other";
import { SkeletonSelect } from "../Skeletons";
import { listBase } from "@/services/api.service";
import {
    Select,
    SelectContent,
    SelectGroup,
    SelectItem,
    SelectTrigger,
    SelectValue,
} from "@/components/ui/select";

interface Props {
    defaultValue?: string;
    onChange: (value: number) => void;
    pluranName: string;
    name: string;
}

const BaseSelect = React.forwardRef<HTMLButtonElement, Props>(({ defaultValue, onChange, pluranName, name }, ref) => {
    const fetchData = async () => await listBase(pluranName);
    const { data, isLoading } = useQuery({ queryKey: [pluranName], queryFn: fetchData });
    if (isLoading) return <SkeletonSelect />;

    return (
        <Select onValueChange={(item) => onChange(parseInt(item))}>
            <SelectTrigger ref={ref} className="w-full ">
                <SelectValue placeholder={defaultValue ? defaultValue : name} />
            </SelectTrigger>
            <SelectContent>
                <SelectGroup>
                    {data.map((item: ILBase, index: number) => (
                        <SelectItem key={index} value={item.id.toString()}>{item.name}</SelectItem>
                    ))}
                </SelectGroup>
            </SelectContent>
        </Select>
    );
});

BaseSelect.displayName = 'BaseSelect';

export default BaseSelect;
