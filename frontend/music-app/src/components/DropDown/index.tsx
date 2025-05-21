"use client";

import { useEffect, useRef, ReactNode } from "react";

interface DropDownInterface {
  isOpen: boolean;
  setIsOpen: (open: boolean) => void;
  trigger: ReactNode;
  children: ReactNode;
}

const DropDown: React.FC<DropDownInterface> = ({
  isOpen,
  setIsOpen,
  trigger,
  children,
}) => {
  const dropDownRef = useRef<HTMLDivElement>(null);

  const handleDropDown = () => {
    setIsOpen(!isOpen);
  };

  useEffect(() => {
    const hanldeClickOutside = (event: MouseEvent) => {
      if (
        dropDownRef.current &&
        !dropDownRef.current.contains(event.target as Node)
      ) {
        setIsOpen(false);
      }
    };
    if (isOpen) {
      document.addEventListener("mousedown", hanldeClickOutside);
    }
    return () => {
      document.removeEventListener("mousedown", hanldeClickOutside);
    };
  }, [isOpen, setIsOpen]);

  return (
    <div className="relative" ref={dropDownRef}>
      <div onClick={handleDropDown} className="cursor-pointer">
        {trigger}
      </div>
      {isOpen && (
        <div className="absolute mt-2 border-[#5e5e5e] border-[0.5px] rounded-[4px] z-2">
          {children}
        </div>
      )}
    </div>
  );
};

export default DropDown;
