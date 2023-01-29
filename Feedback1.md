---
Use case model
---
- rendre le tableaux plus lisible

- ugManageExercise (add exercise, delete exrcise)
- <<>> - UML steryoptype 
- ajouter le nom de use case (in top)
- les cardinalites - how many times are functions executed during the use case () execution
(0..*)

The remaining 4 points depend on the consistency 
- do two use case instances: 1 until login , 1 for the game itself
the input/output events in use case inctanse should be consistent with the use case model
Use case instance - 14,  16/18 if I add a second instance 

---
Env
---

- should not use primitive types,
- should not use class types 

- les input/output -> chaines de characteres
- cest le concept qui nous interesse 
- deux int (score, user number) - different output
- les noms sont pas tres bon, 
e.g. ie[SolutionEntered]ConfirmationMessage

- y en a pas toujour besoin de parameter for ConfirmMessage - always the same message

---
Concept Model
---

- Inheritance uses white arrow

CT suggestion:

ctAnswer (dtAnswer)-> ctExercise(task, solution)

session -> -ctstudent ->ctAnswer

10/11 - unnecessary data, ambiguities between concepts
- remove day
- modify model more correctly

- session History concept
- list modifications in the newer versions

---
Operation Model
---

- Evaluate student 
PostP - "User score is updated" -> functional

- should not have technical expressions (programatical) in the requirements 
(it is design)

operation model should use the same terms as the previous models (concept model)
- when we evaluate student - we don't store the solutions - we "evaluate"
ctAn
mapping NumEtudiant, question, reponse
Enter solution post condition : a solution stored

The solution for a question number N

- Evaluate student - the solution is already stored 

- no technical terms
- precise descriptions 
e.g. a register with score for each exercise and a score associated to a student is stored which is a sum of all score values

ctRegister
ctStudent
ctExercise
ctReponse

- return type, parameters - not programming terms - specifcation terms
- return type - what is sent to tge client (what does the user see after the function is executed)
- prameters - what the user give when he calls the function
setStudyPlan - more a user goal than an operation

- corectness of what is in each table
- too functional description
- confusion between oe and ug

consistency between RA anc code
- functions that are in the code but not in the RA (you can comment why some are in RA but not in the code/ out)

assessment code// RA
