export interface IBase {
    name:string
}
export interface ILBase extends IBase {
    id:number
}

export interface IAttendace {
    career_id: number,
    course_id: number,
    date: string,
    section_id:number
}
export interface ILattendace extends IAttendace {
    id:number
}