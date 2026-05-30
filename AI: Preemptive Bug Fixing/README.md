# AI: Preemptive Bug Fixing

## Project Overview
This task demonstrates the application of structural prompt engineering to utilize generative AI as an industrial-grade static code analysis tool. By assigning role-based contexts, the model was leveraged to preemptively identify semantic vulnerabilities and runtime memory risks in a standard C singly linked list implementation.

## AI Tool Utilized
- **Engine**: Gemini
- **Prompt Framework**: Role-Based Structured Review Model (Senior C Developer Persona)

## Files Included
- `vulnerable_code.c`: Initial implementation containing memory safety failures and a pointer scoping logic bug.
- `refactored_code.c`: Clean, production-ready implementation generated via AI analysis incorporating rigid input validation and layout handling.
