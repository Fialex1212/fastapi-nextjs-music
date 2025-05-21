"use client";

import { useRouter } from "next/navigation";
import { useState } from "react";

const SearchBar = () => {
  const [searchValue, setSearchValue] = useState("");
  const router = useRouter();

  const handleSearchValue = (event: React.ChangeEvent<HTMLInputElement>) => {
    setSearchValue(event.target.value);
  };

  const hanldeSubmit = (event: React.FormEvent<HTMLFormElement>) => {
    event?.preventDefault();
    if (!searchValue.trim()) return;
    router.push(`/search?q=${encodeURIComponent(searchValue.trim())}`);
  };

  return (
    <div>
      <form className="bg-[#4d4c4c] p-1.5 rounded-[4px] w-[400px]" onSubmit={hanldeSubmit}>
        <label>
          <input
            type="text"
            name="Search"
            id="Search"
            placeholder="Search..."
            value={searchValue}
            onChange={handleSearchValue}
            aria-label="Search"
          />
        </label>
      </form>
    </div>
  );
};

export default SearchBar;
