import Link from 'next/link'
 
export default function NotFound() {
  return (
    <div className='container flex flex-col justify-center items-center gap-2 mt-[300px]!'>
      <h2 className='text-[40px]'>Not found 404</h2>
      <p className='text-[24px] max-w-[300px] text-center'>Could not find requested page, track or user</p>
      <Link className='py-2 px-4 bg-white rounded-[4px] text-black font-bold' href="/support">Help me</Link>
    </div>
  )
}