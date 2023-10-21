# GoodBooks - Cross Platform Application

GoodBooks is a cross-platform application built with React Native and Expo. The application is designed to simplify the process of discovering and managing books for avid readers. It allows users to import their GoodReads books, receive personalized recommendations, provide feedback, and manage their reading profile.

## Features

- **Import GoodReads Books:** Users can import their GoodReads books in one click by providing their GoodReads profile URL. A loading animation is displayed during the import process. After successful import, users can view and un-select their imported books.

- **Receive Recommendations:** Users can receive personalized book recommendations based on their GoodReads shelves. A loading animation is displayed while the recommendations are being generated.

- **Provide Feedback:** Users can provide feedback on recommendations in natural language. The feedback is processed by ChatGPT and used to generate new recommendations. A loading animation is displayed while the new recommendations are being generated.

- **View Profile:** Users can view their profile, which includes their imported books, recommendations, and feedback.

## Architecture

The application is organized into two main directories: `components` and `screens`.

- `components`: This directory contains reusable components that are used across different screens.
  - `BookCard.component.ts`: Displays a book with its title, author, cover image, and other relevant details.
  - `FeedbackForm.component.ts`: Provides a form for users to provide feedback in natural language.
  - `LoadingAnimation.component.ts`: Displays a loading animation.
  - `Profile.component.ts`: Displays user profile information, including the user's name, profile picture, and a list of their imported books.
  - `RecommendationCard.component.ts`: Displays a book recommendation, including the book details and additional information about why the book was recommended.

- `screens`: This directory contains the different screens that users can navigate to.
  - `BookImport.screen.ts`: Allows users to provide their GoodReads profile URL and start the import process. It uses the `LoadingAnimation` component while waiting for the import to finish, and the `BookCard` component to display the imported books.
  - `ProfileDetail.screen.ts`: Allows users to view their profile and their imported books. It uses the `Profile` component to display the user profile, and the `BookCard` component to display the imported books.
  - `RecommendationCreate.screen.ts`: Allows users to receive book recommendations and provide feedback on them. It uses the `LoadingAnimation` component while waiting for the recommendations, the `RecommendationCard` component to display the recommendations, and the `FeedbackForm` component for the feedback input.

## Frameworks and Libraries

- **React Native:** A popular framework for building cross-platform applications using JavaScript and React.

- **Expo:** A set of tools and services built around React Native to help developers build, deploy, and quickly iterate on iOS, Android, and web apps.

## Getting Started

To get started with the development:

1. Clone the repository: `git clone https://github.com/your-repo/goodbooks.git`
2. Navigate into the directory: `cd goodbooks`
3. Install the dependencies: `yarn install`
4. Start the Expo development server: `expo start`

Please ensure you have Node.js, yarn, and Expo CLI installed on your machine.


Hallo, ich bin Ahmed.

Ägypten groß geworden, deutsche Schule.
Meine Karriere begann früh, als ich noch Informatik studierte und bereits Produkte für verschiedene Unternehmen entwickelte. Nach meinem Studium ging ich zur RWTH Aachen, wo ich als wissenschaftlicher Mitarbeiter ein neues Masterprogramm an der Schnittstelle von Ethik, Informatik und Psychologie mit aufbaute und meine erste wissenschaftliche Arbeit veröffentlichte.
Das Leben an der Uni war toll, aber nach ein paar Jahren kam Uber auf mich zu und ich war neugierig, also stieg ich ein. Dort war ich derjenige, der das Unmögliche möglich machte, wenn die Geschäftsführer von den Ingenieurteams hörten, dass etwas nicht machbar sei. Heute leite ich die Tech bei Biddz.