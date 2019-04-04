1. Write a Python function that takes two lists and returns True if they have at least one common member.
  ```python
  def test_union(list1, list2):
    has_union = false
    #your code here

    return  has_union

  # test_union([1,2,3], [5,8,1]) should return true as it has common item 1
  #  test_uniont([""])
  ```


2. Implement a function that splits a list into chunks of n items and returns a list of those chunks.
  ```python
  def chunkify(a_very_long_list, limit):
    chunkified_very_long_list = []
    #your code here

    return chunkified_very_long_list

  # chunkify([1,2,3,4,5,6,6,7,8,12,13,90, 14], 4) should return [[1,2,3,4],[5,6,6,7],[8,12,13,90],[14]]
  ```

3. Given json array of Person{dictionary} with properties(name, father, mother), and considering every person has unique name and all couples are conventional couples:
```
example data
population = [
  {
    "name": "Mrs Sanchez",
    "father": "",
    "mother": ""
  },
  {
    "name": "Mr Sanchez",
    "father": "",
    "mother": ""
  },
  {
    "name": "Rick Sanchez",
    "father": "Mr Sanchez",
    "mother": "Mrs Sanchez"
  },
  {
    "name": "Beth Sanchez",
    "mother": "",
    "father": "Rick Sanchez",
    "mother": "Diane Sanchez"
  },
  {
    "name": "Diane Sanchez",
    "father": "",
    "mother": ""
  },
  {
    "name": "Morty Smith Sr",
    "mother": "Beth Sanchez",
    "father": "Jerry Smith"
  },
  {
    "name":  "Jerry Smith",
    "mother": "Joyce Smith",
    "father": "Leonard Smith"
  },
  {
    "name": "Joyce Smith",
    "mother": "",
    "father": ""
  },
  {
    "name": "Leonard Smith",
    "mother": "",
    "father": ""
  },
  {
    "name": "Summer Smith",
    "mother": "Beth Sanchez",
    "father": "Jerry Smith"
  },
  {
    "name": "Morty Jr",
    "mother": "Gwendolyn",
    "father": "Morty Smith Sr"
  },
  {
    "name": "Gwendolyn",
    "mother": "",
    "father": ""
  }
]
```

  - write a function that returns a parents provided their name.
  ```python
  find_person("Morty Smith Sr")
  #returns
  {
    "name": "Morty Smith Sr",
    "mother": "Beth Sanchez",
    "father": "Jerry Smith"
  }
  ```

  - write a function that finds if second argument of a function is mother of first argument.
  ```python
  is_mother("Morty Smith Sr", "Beth Sanchez") # returns true
  is_mother("Morty Smith Sr", "Jerry Smith") # returns false
  ```

  - write a function that finds if second argument of a function is father of first argument.
  ```python
  is_mother("Morty Smith Sr", "Beth Sanchez") # returns false
  is_mother("Morty Smith Sr", "Jerry Smith") # returns true
  ```

  - write a function that returns Parents' dictionary.
  ```python
  find_parents(
      "Morty Smith Sr"
  )
  # should return {
  "mother": "Beth Sanchez",
  "father": "Jerry Smith"
  }
  ```

  - write a function that finds if two individuals are siblings.
  ```python
  are_siblings("Morty Smith Sr", "Summer Smith") # returns true
  are_siblings("Morty Smith Sr", "Jerry Smith") # returns false
  ```

  - write a function that finds siblings; half(one parent is same) and full(both parents are same), of an individual.
  ```python
  find_siblings("Morty Smith Sr")
  # returns
  {
    full: ["Summer Smith"],
    half: []
  }
  ```

  - write a function that parses up generation till the known root with respect to male generation.
  ```python
  parse_up_male_generation("Summer Smith") 
  # prints
  Jerry Smith is father of Morty Smith Sr
  Leonard Smith is Father of Jerry Smith
  Leonard Smith's father is not known
  ```

  - write a function that parses up generation till the known root with respect to female generation.
  ```python
  parse_up_male_generation("Summer Smith") 
  # prints
  Beth Sanchez is mother of Summer Smith
  Diane Sanchez is mother of Beth Sanchez
  Diane Sanchez's mother is not known
  ```

  _Notice that some values are empty strings. consider those cases as unknown case and return primitive value of those structure: "" for strings, {} for dictionaries and [] for arrays_
