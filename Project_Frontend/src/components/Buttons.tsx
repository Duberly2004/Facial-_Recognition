import { Pencil, Trash2 } from 'lucide-react'
import { Button } from './ui/button'
import React from 'react'

interface Props {
  onClick: () => void
  title?: string
}

export const ButtonDelete = ({ title, onClick }: Props) => {
  return (
    <Button className='text-gray-500 bg-transparent hover:bg-transparent gap-1 hover:text-color_primary_2' size={'sm'} onClick={onClick}><Trash2 className='w-4 text-color_primary_2' />{title}</Button>
  )
}

export const ButtonEdit = React.forwardRef<HTMLButtonElement, Props>((props, ref) => {
  const { onClick } = props;
  return (
    <Button ref={ref} {...props} className='text-gray-500 bg-transparent hover:bg-transparent gap-1 hover:text-color_primary_2' size={'sm'} onClick={onClick}>
      <Pencil className='w-4 text-color_primary_2' />
      {props.title}
    </Button>
  );
});

