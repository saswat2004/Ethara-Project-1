**Prompt:** **Advanced Scientific & Engineering Calculator**

**Context and Role**:

You are a Full-Stack Developer who is specialised in computational tools and modern web experiences, you are responsible for designing and implementing a high-performance, advanced web-based calculator. The application must handle complex mathematical operations  
Maintain a responsive ,accessible, and production-level user interface. The calculator should go beyond basic arithmetic to serve as a comprehensive tool for advanced mathematics, guiding the user through calculations with a clean, intuitive layout.

**Objective:**

Develop a complete, robust advanced calculator application that will implement a powerful mathematical parsing engine capable of handling standard and advanced concepts.  
Provides a modern and responsive UI with smooth interactive transitions.  
Includes a "Calculation History" sidebar and a dynamic graphing module.  
Logs complex errors securely without crashing the application.

**Mathematical Requirements:**

The core engine must accurately compute and support the following concepts:  
Basic & Advanced Arithmetic:  
Fractions, percentages, permutations and combinations.  
Algebra & Functions:  
Polynomials , linear equations ,exponential growth and logarithmic functions (base $e$ and base 10).  
Trigonometry:  
Sine, cosine ,tangent and their inverses with a toggle for Degrees/Radians/Gradians.  
Calculus & Matrices:  
Support for basic symbolic differentiation ,definite integrals and matrix operations (addition, multiplication, determinants).  
Complex Numbers:  
Standard operations involving real and imaginary components ($a \+ bi$).

**UI and Animation Requirements:**  
**Interactive Layout**  
Implement state-triggered micro-interactions for button presses and mathematical output rendering.  
Include smooth transitions between layout states (e.g. expanding the scientific keypad or opening the graphing tab).  
Ensure UI animations are performant , avoiding layout thrashing and utilizing GPU-friendly properties.

**Layout Requirements**  
The interface must include:  
A primary dynamic display for current inputs and real-time calculation previews and a secondary animated text reveals for the "History" panel, showing past calculations.  
A responsive keypad section with distinct visual states (hover, active, disabled) with a fully responsive behavior across mobile ,tablet, and desktop viewports.  
Accessibility compliance utilizing ARIA labels for screen readers.

**Backend and Logic Processing Requirements:**

Implement a client-side or server-side API endpoint for heavy mathematical processing (e.g. rendering large graphs or solving complex symbolic calculus).  
Sanitize all mathematical inputs to prevent injection attacks (e.g. executing arbitrary JavaScript via eval()).  
Utilize a safe and established math evaluation library rather than native string evaluation.  
Ensure the mathematical API or logic block returns structured JSON responses detailing the computed result, computation time and any precision warnings.

**Output Requirements:**  
A smoothly animated and instant responsive calculator interface.  
Graceful handling of mathematical impossibilities (e.g. division by zero ,negative square roots in real-number mode).  
Confirmation or distinct visual cues upon saving a result to the history log.

**Error Handling and Documentation:**  
Handle frontend syntax errors gracefully , providing real-time feedback (e.g, "Missing closing parenthesis").  
Provide structured error responses rather than application crashes when complex inputs fail.  
Document the repository thoroughly, including:  
Folder structure.  
Setup instructions and environment variable configuration.  
Deployment steps.

**Performance and Scalability:**  
Optimize the overall bundle size ,specifically lazy-loading heavy graphing or symbolic math libraries until requested by the user.  
Use proper debouncing for user interactions, especially when rendering graphs in real-time based on equation input.  
Ensure that any backend components can support concurrent calculations without API bottlenecks.

**Technology Stack:**  
Use the following tech stacks:  
Frontend: React or Next.js.  
Styling & Animation: Tailwind CSS combined with Framer Motion for UI fluidity.  
Math Engine: Math.js (for extensive client-side calculation capability) or SymPy (if using a Python in backend).  
Backend (Optional for heavy logic): Node.js with Express , or Next.js API routes.  
Storage (Optional): Browser LocalStorage for persistent history ,or PostgreSQL if building a cloud-synced account system.

