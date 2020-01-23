const recipes = [
  {
    key: "asian-dumpling-sauce",
    name: "Asian Dumpling Sauce",
    sections: [
      {
        type: "ingredients",
        items: [
          "1/4 cup soy sauce",
          "1/4 cup rice wine vinegar",
          "1 tablespoon honey",
          "2 cloves minced garlic",
          "2 teaspoons minced ginger",
          "1 teaspoon sesame seeds",
          "1 teaspoon sesame oil",
        ],
      },
      {
        type: "directions",
        items: ["mix together"],
      },
    ],
  },
  {
    key: "broccoli-casserole",
    name: "Broccoli Casserole",
    sections: [
      {
        type: "ingredients",
        items: [
          "2 bunches of broccoli (~300g)",
          "1 can cream of mushroom soup",
          "250ml sour cream",
          "1 tablespoon minced onion",
          "1 cup shredded cheddar cheese",
          "15 Ritz crackers, crushed",
        ],
      },
      {
        type: "directions",
        items: [
          "Cook broccoli until tener, and drain well",
          "Mix with all other ingredients",
          "Bake for 20 minutes at 350F",
        ],
      },
    ],
  },
  {
    key: "broccoli-slaw-salad",
    name: "Broccoli Slaw Salad",
    sections: [
      {
        type: "ingredients",
        items: [
          "2 packs of beef Mr. Noodles",
          "4 green onions",
          "1 cup roasted/salted sunflower seeds",
          "1/2 cup sugar",
          "3/4 cup oil",
          "1/3 cup vinegar",
        ],
      },
      {
        type: "directions",
        items: [
          "smash up the dry noodles",
          "chop the green onions",
          "mix everything together",
        ],
      },
    ],
  },
  {
    key: "butternut-squash-casserole",
    name: "Butternut Squash Casserole",
    sections: [
      {
        type: "ingredients",
        items: [
          "1 large onion",
          "2 stalks celery",
          "2 carrots",
          "2 potatoes",
          "1 butternut squash",
          "1L chicken broth",
          ".5t cayenne pepper",
          "1T yellow curry powder",
          ".5C sour cream",
          "salt",
          "pepper",
          "butter",
        ],
      },
      {
        type: "directions",
        items: [
          "Roast the butternut squash (whole, peel on) for 1 hour at 375F",
          "Finely chop all vegetables",
          "Melt some butter in a large pot, and fry the vegetables until lightly browned (~5 minutes)",
          "Pour in enough of the chicken broth to cover the vegetables",
          "Add cayenne, curry, salt, pepper",
          "Add the butternut squash",
          "Bring to a boil, reduce heat, cover, simmer for ~45 minutes",
          "Blend soup until smooth",
          "Add remaining chicken broth until desired consistency",
          "Mix in sour cream",
        ],
      },
    ],
  },
  {
    key: "chicken-broccoli-casserole",
    name: "Chicken Broccoli Casserole",
    sections: [
      {
        type: "ingredients",
        items: [
          "500g broccoli, chopped (4ish cups)",
          "1 large onion, chopped",
          "2 stalks celery, chopped",
          "1-2 cups chicken broth",
          "1 can (~150ml) water chestnuts, drained",
          "1 can cream of mushroom soup",
          "1 can sliced mushrooms, drained",
          "1 cup uncooked rice (2ish cups cooked)",
          "2-3 chicken breasts",
          "1 cup shredded cheddar cheese",
          "1/4 cup butter",
          "1 tbsp garlic powder",
          "salt, pepper",
        ],
      },
      {
        type: "directions",
        items: [
          "Cube and cook the chicken separately",
          "Cook the rice separately",
          "Melt the butter in a large skillet and saute the onion and celery",
          "Slowly add chicken broth to the saute and continue until celery is somewhat tender",
          "Stir in the soup and remaining chicken broth",
          "Add the broccoli, water chestnuts, mushrooms, rice, and chicken",
          "Add garlic powder, salt, and pepper",
          "Cook for about 5 minutes",
          "Mix in the cheese, spread in a 9x13 baking dish and bake for 30 minutes at 325F",
        ],
      },
    ],
  },
  {
    key: "chili",
    name: "Chili",
    sections: [
      {
        type: "ingredients",
        items: [
          "2 pounds ground beef",
          "4 (15 ounce) cans various chili beans, drained",
          "2 (28 ounce) cans diced tomatoes with juice",
          "1 (6 ounce) can tomato paste",
          "1 (~300ml) can sliced mushrooms",
          "1 large yellow onion, chopped",
          "3 stalks celery, chopped",
          "2 bell peppers, seeded and chopped",
          "2 green chili peppers, seeded and chopped",
          "4 cubes beef bouillon",
          "1/2 cup beer",
          "1/4 cup chili powder",
          "1 tablespoon Worcestershire sauce",
          "1 tablespoon minced garlic",
          "1 tablespoon dried oregano",
          "2 teaspoons ground cumin",
          "2 teaspoons hot pepper sauce (e.g. Tabasco)",
          "1 teaspoon dried basil",
          "1 teaspoon salt",
          "1 teaspoon ground black pepper",
          "1 teaspoon cayenne pepper",
          "1 teaspoon paprika",
        ],
      },
      {
        type: "directions",
        items: [
          "In a large stock pot, cook the ground beef until evenly browned and drain off extra grease",
          "Add chili beans, diced tomatoes, tomato paste, all chopped veggies, bouillon, beer, and remaining spices",
          "Stir to blend, then cover and simmer over low heat for 2 hours. Stir occasionally",
          "Taste, and add salt/pepper/chili powder, if necessary",
        ],
      },
    ],
  },
  {
    key: "christmas-morning-saver",
    name: "Christmas Morning Saver",
    sections: [
      {
        type: "ingredients",
        items: [
          "~16 slices of bread, crust removed",
          "slices of ham or Canadian back bacon",
          "slices of sharp cheddar cheese",
          "6 eggs",
          "1/4 cup minced onion",
          "1/4 cup green pepper, finely chopped",
          "1/2 teaspoon pepper",
          "1/2 teaspoon salt",
          "1 teaspoon dry mustard",
          "2 teaspoons Worchestershire sauce",
          "3 cups milk",
          "Tabasco sauce to taste",
          "1/2 cup butter",
          "Special K or similar dry cereal",
        ],
      },
      {
        type: "directions",
        items: [
          'Butter a 9"x13" glass baking dish, and cover with a layer of bread slices.',
          "Cover the bread layer with slices of ham.",
          "Cover the ham layer with slices of cheese.",
          "Finish with a layer of bread, making a giant sandwich.",
          "In a bowl, beat eggs, salt, and pepper.",
          "Add dry mustard, onion, green pepper, Worchestershire, milk, and Tabasco.",
          "Pour the egg mixture over the sandwiches.",
          "Cover and refrigerate overnight.",
        ],
      },
      {
        type: "directions",
        items: [
          "Melt 1/2 cup of butter, and pour over egg sandwiches.",
          "Cover with Special K.",
          "Bake for 45 minutes, at 325F.",
          "Let stand for 10 minutes before serving.",
        ],
      },
    ],
  },
  {
    key: "dak-galbi",
    name: "Dak Galbi",
    sections: [
      {
        type: "ingredients",
        items: [
          "2 tbsp red pepper powder",
          "3 tbsp red pepper paste",
          "4 tsp curry powder",
          "3 cloves minced garlic",
          "3 tbsp soy sauce",
          "2 tbsp cooking wine",
          "2 tbsp minced ginger",
          "black pepper",
        ],
      },
      {
        type: "ingredients",
        items: [
          "2 chicken breasts",
          "1 tbsp cooking wine",
          "2 cloves minced garlic",
          "black pepper",
        ],
      },
      {
        type: "ingredients",
        items: [
          "4 green onions",
          "3 onions",
          "1/2 head of cabbage",
          "2 sweet potatoes",
          "1 package of Asian rice cakes (650g)",
          "water",
          "olive oil",
          "sesame oil",
          "sesame seeds",
        ],
      },
      {
        type: "directions",
        items: [
          "Chop up chicken, mix with the chicken ingredients, set aside",
          "Soak rice cakes until thawed",
          "Mix up sauce ingredients in a bowl, add 1/3 of this sauce to the marinating chicken, and set aside",
          "Chop onions, cabbage, and sweet potato into thin, bite-sized pieces",
          "Pour equal amounts of sesame and olive oil in a hot wok",
          "Fry cabbage, onion, sweet potato, and rice cakes (cover and add water) until they are tender",
          "Add in chicken and remaining sauce",
          "Near the end, add in chopped green onion",
          "Add sesame seeds",
        ],
      },
    ],
  },
  {
    key: "dill-pickle-soup",
    name: "Dill Pickle Soup",
    sections: [
      {
        type: "ingredients",
        items: [
          "5-1/2 cups chicken broth",
          "6-1/2 cups russet potatos, peeled and cubed",
          "2 cups chopped carrots",
          "1 cup chopped dill pickles",
          "1/2 cup unsalted butter",
          "1/2 cup all-purpose flour",
          "1 cup sour cream",
          "1/4 cup water",
          "2 cups dill pickle juice",
          "1-1/2 teaspoons Old Bay seasoning",
          "1/2 teaspoon table salt (depending on how salty your pickle juice is)",
          "1/2 teaspoon coarsely ground pepper",
          "1/4 teaspoon cayenne pepper",
        ],
      },
      {
        type: "directions",
        items: [
          "In a large pot, combine broth, potatoes, carrots and butter. Bring to a boil and cook until the potatoes are tender.",
          "Add pickles and continue to boil.",
          "In a medium bowl, stir together flour, sour cream and water, making a paste.",
          "Whisk sour cream mixture (a couple tablespoons at a time) into soup.",
          "Add pickle juice, Old Bay, salt, pepper and cayenne.",
          "Cook 5 more minutes and remove from heat.",
        ],
      },
    ],
  },
  {
    key: "eggplant-minced-pork",
    name: "Eggplant Minced Pork",
    sections: [
      {
        type: "ingredients",
        items: [
          "400g ground pork",
          "1 tablespoon soy sauce",
          "1 teaspoon pepper",
          "1 tablespoon sesame oil",
          "4 cloves garlic",
          "3 Japanese eggplants, diced",
          "150ml chicken stock",
          "3 tablespoons chilli bean paste (doubanjiang)",
          "1 teaspoon vinegar",
          "1 teaspoon fish sauce",
          "1 teaspoon sesame oil",
          "2 green onions (optional)",
        ],
      },
      {
        type: "directions",
        items: [
          "Mix pork mince with soy sauce, pepper and sesame oil then marinate for at least 10 minutes",
          "Heat 2 tablespoons of oil in a preheated wok. Sauté half of the garlic until fragrant",
          "Add the eggplant. Gradually stir in the stock, stir-fry until the eggplant turns from purple to brown, remove and set aside",
          "Heat a tablespoon of oil in the hot wok, sauté the other half of the garlic until fragrant. Add minced pork and stir-fry until opaque",
          "Add chilli bean paste, eggplant, vinegar, fish sauce and sesame oil then stir well. Sprinkle in green onions and serve",
        ],
      },
    ],
  },
  {
    key: "festive-turnip",
    name: "Festive Turnip",
    sections: [
      {
        type: "ingredients",
        items: [
          "1 large rutabaga",
          "2 cooking apples (i.e. Cortland)",
          "2 tablespoons butter",
          "1/4 cup brown sugar",
          "a dash of cinnamon",
        ],
      },
      {
        type: "ingredients",
        items: ["1/3 cup brown sugar", "1/3 cup flour", "2 tablespoons butter"],
      },
      {
        type: "directions",
        items: [
          "Peel and dice the turnip, and boil until tender.",
          "Drain, and mash with butter.",
          "Peel and slice the apples, and mix with brown sugar and cinnamon.",
          "In a greased baking dish, spread 1/2 of the turnip.",
          "Add the apple mixuture ad the next layer.",
          "Add the remaining turnip as the next layer.",
          "In a small bowl, mix brown sugar, flour, and butter until crumbly.",
          "Sprinkle on top of turnip.",
          "Bake for 1 hour at 350F.",
        ],
      },
    ],
  },
  {
    key: "grilled-sweet-potato",
    name: "Grilled Sweet Potato",
    sections: [
      {
        type: "ingredients",
        items: [
          "2 sweet potatoes",
          "2 tbsp olive oil",
          "2 tbsp brown sugar",
          "1 tbsp cumin",
          "1 tsp cayenne",
          "salt and pepper",
        ],
      },
      {
        type: "directions",
        items: [
          "Cut up potatoes, and mix all ingredients in a bowl",
          "Wrap in aluminium foil pouch",
          "Cook on BBQ for ~25 minutes, turning 2-3 times throughout",
        ],
      },
    ],
  },
  {
    key: "leek-potato-soup",
    name: "Leek Potato Soup",
    sections: [
      {
        type: "ingredients",
        items: [
          "2+ tbsp butter",
          "2 leeks, chopped",
          "1 large onion, chopped",
          "5 cups potatoes, peeled and cubed",
          "4 cups chicken broth",
          "1 cup blend cream (10%)",
          "1+ teaspoon garlic powder",
          "salt and pepper",
        ],
      },
      {
        type: "directions",
        items: [
          "Melt butter in a pot over medium heat",
          "Cook and stir leeks and onion until vegetables are tender, about 5 minutes",
          "Add potatoes and chicken broth and simmer until potatoes are tender, about 20 minutes",
          "Add cream, and simmer until slightly thickened, about 15 minutes",
          "Blend (optional) and add garlic powder, salt, and pepper, and simmer for another 5 minutes",
        ],
      },
    ],
  },
  {
    key: "minty-cookies",
    name: "Minty Cookies",
    sections: [
      {
        type: "ingredients",
        items: [
          "1 cup butter flavored Crisco",
          "1 package (8 oz) cream cheese, softened",
          "3/4 cup granulated sugar",
          "1/2 cup firmly packed brown sugar",
          "1 tsp vanilla",
          "2 cups all-purpose flour",
          "1 3/4 cups mint chocolate chips",
        ],
      },
      {
        type: "directions",
        items: [
          "Heat oven to 375F",
          "Combine Crisco, cream cheese, sugars and vanilla in large bowl",
          "Beat at medium speed of electric mixer until well blended",
          "Mix flour into creamed mixture at low speed until just blended",
          "Stir in mint chocolate chips",
          "Form balls of 3-4cm diameter, and press slightly onto baking sheet",
          "Bake for 11 minutes, or until lightly browned",
          "Cool for 2 minutes on baking sheet, then move to cooling rack",
        ],
      },
    ],
  },
  {
    key: "shrimp-squash-risotto",
    name: "Shrimp Squash Risotto",
    sections: [
      {
        type: "ingredients",
        items: [
          "2 packs of PC 4 cheese risotto (2x170g)",
          "1 butternut squash (~1 pound, cubed)",
          "25 shrimp",
          "garlic (or garlic powder)",
          "salt",
          "pepper",
          "butter",
        ],
      },
      {
        type: "directions",
        items: [
          "Cut butternut squash into bite-size cubes (1-2cm), toss in oil, and roast for ~40 minutes at 375F",
          "Make risotto according to package instructions (basically like KD)",
          "Toss shrimp in oil, salt, pepper, and minced garlic (or garlic powder)",
          "Fry shrimp until fully cooked",
          "Mix everything together, and add pepper to taste",
        ],
      },
    ],
  },
  {
    key: "soy-sriracha-sauce",
    name: "Soy Sriracha Sauce",
    sections: [
      {
        type: "ingredients",
        items: [
          "1 tsp sesame oil",
          "3 tbsp soy sauce",
          "1 tbsp grainy mustard",
          "1+ tsp sriracha sauce",
        ],
      },
      {
        type: "directions",
        items: ["mix together"],
      },
    ],
  },
  {
    key: "vidalia-onion-dip",
    name: "Vidalia Onion Dip",
    sections: [
      {
        type: "ingredients",
        items: [
          "8 oz cream cheese",
          "1/2 cup mayonaise",
          "1 cup vidalia onion, finely chopped",
          "1/4 cup parmesan cheese",
          "1+ tsp Frank's Red Hot",
          "salt",
          "pepper",
          "paprika",
        ],
      },
      {
        type: "directions",
        items: [
          "Mix together, and spread in a shallow baking dish.",
          "Sprinkle with paprika.",
          "Bake for 40 minutes at 350F.",
        ],
      },
    ],
  },
];

export {recipes};