import { useEffect, useState } from "react"
import axios from 'axios'
import { baseurl } from "../utils/config"

export default function Details() {
const [details, setDetails]=useState<{id:number, name:string, age:number, city:string, country:string}[]>([])

const fetchData= async()=>{
    try {
        const response=await axios.get(`${baseurl}/api/details`)
        setDetails(response.data)
        console.log(response.data)
    } catch (error) {
        console.error("Fetch data error:", error);
    }
}

const deleteDetail=async(id:number)=>{
    try {
        await axios.delete(`${baseurl}/api/details/${id}`);
        setDetails((prevDetails) => prevDetails.filter((detail) => detail.id !== id));
        console.log(`Deleted detail with ID: ${id}`);
      } catch (error) {
        console.error("Delete detail error:", error);
      }
}

useEffect(()=>{
    fetchData()
},[])
  return (
    <div>
       <h1>Details</h1>
            <ul>
                {details?.map((detail) => (
                    <li key={detail.id}>
                        {detail.name} - {detail.age} - {detail.city}, {detail.country}    &nbsp;
                        <button onClick={()=>deleteDetail(detail.id)}>Delete</button>
                    </li>
                ))}
            </ul>
    </div>
  )
}
