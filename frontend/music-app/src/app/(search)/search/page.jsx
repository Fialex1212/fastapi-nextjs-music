"use client";

import { useSearchParams } from "next/navigation";

export default function SearchPage() {
  const searchParams = useSearchParams();
  const q = searchParams.get("q");

  return <h1>Search results for: {q}</h1>;
}
