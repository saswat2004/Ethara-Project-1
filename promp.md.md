**Prompt:** **Advanced Scientific & Engineering Calculator**

---

**Context and Role**
As a Full-Stack Developer you are specializing in computational tools and modern web experiences , you are responsible for designing and implementing a high-performance ,advanced web-based calculator. The application must serve as a comprehensive tool for advanced mathematics, guiding the user through complex calculation with a responsive, accessible and production-level user interface.

---

**Objective**
Develop a robust, full-stack calculator application that implements a powerful mathematical parsing engine, provides a modern UI with smooth interactive transitions, features a dynamic graphing module, and securely processes complex equations without application crashes.

---

**Input Data**
Mathematical Inputs (String/JSON payloads) containing:
Standard and complex mathematical expressions
Equation variables and constants
Matrix dimensions and cell values
Integration bounds for calculus operations
Configuration States containing:
Angle unit toggles (Degrees, Radians, Gradians)
Number system modes (Real vs. Complex)

---

**Data Processing Requirements**
Clean and sanitize all mathematical inputs to prevent injection attacks, strictly avoiding unsafe native string execution like eval().
Implement an abstraction layer that parses complex string equations into structured operations for the math engine.
Maintain a secure and persistent "Calculation History" log that updates in real-time as users execute operations.
Manage application state efficiently to handle seamless transitions between standard keypad views, graphing tabs, and matrix input modules.

---

**Mathematical & Feature Requirements**
Implement a core logic for basic arithmetic, fractions, percentages, permutations and combinations.
Develop support for algebra and functions including polynomials, linear equations, exponential growth and logarithmic functions with base e and base 10.
Integrate comprehensive trigonometry functions such as (sine, cosine , tangent and their inverses) tied dynamically to the selected angle unit.
Engineer advanced calculation capabilities for calculus and matrices, supporting symbolic differentiation, definite integrals and matrix arithmetic such as (addition, multiplication ,determinants etc).
Support operations involving complex numbers with distinct real and imaginary components (a + bi).
Build an accessible , fully responsive UI utilizing ARIA labels and distinct visual states (hover, active, disabled) across mobile , tablet and desktop viewports.

---

**Output Requirements**
Generate a primary dynamic display that shows current inputs alongside real-time calculation previews.
Produce a responsive graphing module that visually plots complex mathematical functions.
Export structured JSON responses from the processing engine detailing the computed result, computation time, and any precision warnings.
Render an animated "History" panel with text-reveal transitions to display past calculations.

---

**Error Handling and Documentation**
Implement real-time frontend validation for syntax errors, providing immediate user feedback (e.g., "Missing closing parenthesis") using Regex and Abstract Syntax Tree (AST) pre-parsing to catch syntax errors before execution.
Handle mathematical impossibilities gracefully through structured error responses (e.g., division by zero, negative square roots in real-number mode) rather than application crashes.
Organize the repository modularly, separating UI components, state management, and mathematical evaluation logic.
Custom Backend Error Classes: Handle mathematical impossibilities (e.g., division by zero, domain errors) using custom server-side error classes (e.g., MathComputationError, ParsingError) that return standardized HTTP status codes and structured JSON payloads rather than causing server crashes.
Document the repository thoroughly, detailing folder structure, environment variable configuration, and deployment steps.

---

**Performance and Scalability**
Optimize the application's bundle size by lazy-loading heavy graphing or symbolic math libraries only when requested by the user.
Implement proper debouncing for user interactions, specifically optimizing real-time graph rendering as the user types an equation.
Ensure UI animations are performant, utilizing GPU-friendly properties to avoid layout thrashing during state changes.
Architect backend or Web Worker components to support concurrent, heavy mathematical processing without bottlenecking the main thread.

---

**Tools and Libraries**
Use the following technologies :
React or Next.js for the frontend architecture .
Tailwind CSS combined with Framer Motion for styling , responsive layout, and UI fluidity.
Math.js (for client-side processing) or SymPy (if processing via a Python backend) for the core mathematical engine .
Node.js with Express or Next.js API routes for heavy logic processing.
Browser LocalStorage (for local history persistence) or PostgreSQL (for cloud-synced user accounts).
