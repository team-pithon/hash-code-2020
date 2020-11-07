# Google Hash Code 2020

## Practice Round: [More Pizza](practice-round/more_pizza.pdf)

### Problem Statement:

The goal is to

```
order as many pizza slices as possible, but not more than the maximum number.
```

### How we tackled the problem:

- 1st attempt: We order pizzas *from smallest to largest* until no pizza is small enough to not exceed the goal.

- 2nd attempt: We order pizzas *from largest to smallest* until the next pizza exceeds the goal and then order pizzas *from smallest to largest* until no pizza is small enough to not exceed the goal.

- 3rd attempt: We order pizzas *at random* until no pizza is small enough to not exceed the goal.

---

## Online Qualification Round / Extended Round: [Book Scanning](qualification-round/book_scanning.pdf)

### Problem Statement:

The goal is to

```
Given a description of libraries and books available, plan which books to scan from which library to maximize the total score of all scanned books, taking into account that each library needs to be signed up before it can ship books.
```

### How we tackled the problem:

#### Online Qualification Round:


| Attempt | What Libraries? | How? | What Books? | How? |
| :-------| :-------------- | :--- | :---------- | :--- |
| 1st     | first n so that the sum of their signup cost was no greater than the total number of days available | in the order of the input file | all books | in the order of the input file |
| 2nd     | first n so that the sum of their signup cost was no greater than the total number of days available | sorted by increasing signup time | all books | sorted by decreasing book score |
| 3rd     | first n so that the sum of their signup cost was no greater than the total number of days available | sorted by increasing signup time | only the books which would actually be scanned and wouldn't be scanned by previous libraries | sorted by decreasing book score |
| 4th     | first n so that the sum of their signup cost was no greater than the total number of days available | sorted by increasing (mistake!) rank (all books score, signup time) (badly implemented!) | only the books which would actually be scanned and wouldn't be scanned by previous libraries | sorted by decreasing book score |
| 5th     | first n so that the sum of their signup cost was no greater than the total number of days available | at random | only the books which would actually be scanned and wouldn't be scanned by previous libraries | sorted by decreasing book score |
| 6th     | first n so that the sum of their signup cost was no greater than the total number of days available | sorted by increasing (mistake!) number of books | only the books which would actually be scanned and wouldn't be scanned by previous libraries | sorted by decreasing book score |
| 7th     | first n so that the sum of their signup cost was no greater than the total number of days available | sorted by increasing (mistake!) all books score | only the books which would actually be scanned and wouldn't be scanned by previous libraries | sorted by decreasing book score |

#### Extended Round:

| Attempt | What Libraries? | How? | What Books? | How? |
| :-------| :-------------- | :--- | :---------- | :--- |
| 1st     | first n so that the sum of their signup cost was no greater than the total number of days available | sorted by decreasing rank (all books score, signup time) (badly implemented!) | only the books which would actually be scanned and wouldn't be scanned by previous libraries | sorted by decreasing book score |
| 2nd     | first n so that the sum of their signup cost was no greater than the total number of days available | sorted by decreasing number of books | only the books which would actually be scanned and wouldn't be scanned by previous libraries | sorted by decreasing book score |
| 3rd     | first n so that the sum of their signup cost was no greater than the total number of days available | sorted by decreasing all books score | only the books which would actually be scanned and wouldn't be scanned by previous libraries | sorted by decreasing book score |
| 4th     | first n so that the sum of their signup cost was no greater than the total number of days available | sorted by decreasing rank (all books score, signup time, scanning rate) | only the books which would actually be scanned and wouldn't be scanned by previous libraries | sorted by decreasing book score |
| 5th     | first n so that the sum of their signup cost was no greater than the total number of days available | sorted by decreasing rank (all books score, signup time) | only the books which would actually be scanned and wouldn't be scanned by previous libraries | sorted by decreasing book score |

### Placements:

| Round                      | Score             | #Hub | #Country | #Worldwide |
| :------------------------- | :---------------- | :--- | :------- | :--------- |
| Online Qualification Round | 22,251,419 points | 5th  | 34th     | 3,472th    |
| Extended Round             | 22,859,495 points | 3rd  | 17th     | 1,995th    |

**#HashCodeSolved**

---

# Team πthon:

| Name               | Github                                                       | Role                                     |
| :----------------- | :----------------------------------------------------------- | :--------------------------------------- |
| Cristiano Clemente | [@cristiano-clemente](https://github.com/cristiano-clemente) | Team Leader & Programmer                 |
| Hugo Pitorro       | [@xtwigs](https://github.com/xtwigs)                         | Programmer                               |
| Catarina Carreiro  | [@cmcarreiro](https://github.com/cmcarreiro)                 | Algorithm Designer (& Bug-Finder Person) |
| Mónica Jin         | [@mokita-j](https://github.com/Mokita-J)                     | Algorithm Designer                       |

hub: [GCE - IST](https://www.gce-neiist.org/) from [Instituto Superior Técnico](https://tecnico.ulisboa.pt/en/) (Lisbon, Portugal)
