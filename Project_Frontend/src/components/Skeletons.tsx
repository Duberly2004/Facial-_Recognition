
import { Skeleton } from "@/components/ui/skeleton"

export const SkeletonSelect = ()=> {
  return (
    <div className="flex items-center space-x-4">
        <Skeleton className="h-11 w-full" />
    </div>
  )
}