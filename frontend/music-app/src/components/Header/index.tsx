"use client";

import React, { useState } from "react";
import SearchBar from "../SearchBar";
import Link from "next/link";
import DropDown from "../DropDown";
import { Bell, ChevronDown, Ellipsis, Mail } from "lucide-react";

const Header = () => {
  const user = false;
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [isUserOpen, setIsUserOpen] = useState(false);

  return (
    <div className="container flex justify-center items-center gap-6 h-[50px] font-medium">
      <Link href="/home">Logo</Link>
      <Link href="/home">Home</Link>
      <Link href="/library">Library</Link>
      <SearchBar />
      <div className="">
        {user ? (
          <div className="flex justify-center items-center gap-6">
            <Link href="/upload">Upload</Link>
            <Link className="text-[#f87e24]" href={"/subscription/buy"}>
              Try Pro Subscription
            </Link>
            <DropDown
              isOpen={isUserOpen}
              setIsOpen={setIsUserOpen}
              trigger={
                <div className="flex items-center gap-2 h-[40px]">
                  <div className="rounded-[50%] w-[26px] h-[26px] bg-white"></div>
                  <ChevronDown />
                </div>
              }
            >
              <div className="w-[160px] font-semibold">
                <ul className="p-2">
                  <li className="cursor-pointer flex items-center p-2">
                    Profile
                  </li>
                  <li className="cursor-pointer flex items-center p-2">
                    Likes
                  </li>
                  <li className="cursor-pointer flex items-center p-2">
                    Playlists
                  </li>
                  <li className="cursor-pointer flex items-center p-2">
                    Following
                  </li>
                  <li className="cursor-pointer flex items-center p-2">
                    Tracks
                  </li>
                </ul>
              </div>
            </DropDown>
            <Mail />
            <Bell />
          </div>
        ) : (
          <div className="flex items-center gap-6">
            <Link className="" href={"/sign-in"}>
              Sign in
            </Link>
            <Link
              className="bg-[#ffffff] text-[#000000] p-1 rounded-[4px]"
              href={"/sign-up"}
            >
              Create account
            </Link>
            <Link href="/upload">Upload</Link>
          </div>
        )}
      </div>

      <DropDown
        isOpen={isMenuOpen}
        setIsOpen={setIsMenuOpen}
        trigger={
          <div className="h-[40px] flex justify-center items-center">
            <Ellipsis />
          </div>
        }
      >
        <div className="w-[160px] font-semibold">
          <ul className="p-2">
            <li className="cursor-pointer flex items-center p-2">About us</li>
            <li className="cursor-pointer flex items-center p-2">Blog</li>
            <li className="cursor-pointer flex items-center p-2">Support</li>
            <li className="cursor-pointer flex items-center p-2">Developers</li>
          </ul>
          <div className="w-full h-[1px] bg-[#5e5e5e]"></div>
          <ul className="p-2">
            <li className="cursor-pointer flex items-center p-2">
              Subscription
            </li>
            <li className="cursor-pointer flex items-center p-2">Settings</li>
            <li className="cursor-pointer flex items-center p-2">Sign out</li>
          </ul>
        </div>
      </DropDown>
    </div>
  );
};

export default Header;
