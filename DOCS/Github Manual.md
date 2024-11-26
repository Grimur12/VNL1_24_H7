## Introduction
Git is version control system that allows developers to track changes in their code over time, collaborate with others, and manage software development projects efficiently. Unlike traditional version control systems, Git stores data as snapshots of the entire project rather than just a series of file changes, making it faster and more flexible. It enables multiple developers to work on different parts of a project simultaneously without disrupting each other’s work. Git also allows easy branching and merging, making it ideal for handling different features, fixes, and experiments in parallel. With Git, you can manage your project's history, experiment with code, and roll back to earlier versions as needed.

GitHub Desktop is a graphical user interface (GUI) that simplifies the use of Git for new developers, especially those who prefer not to work with commandline. It integrates with GitHub, a cloud-based platform for hosting Git repositories, making it easier to clone, commit, push, and pull changes from repositories. GitHub Desktop provides a user-friendly interface that helps manage branches, view changes in files, and resolve conflicts. Altough traditionally meant for beginners, both beginners and experienced developers can benefit from using it, GitHub Desktop allows you to work more efficiently with Git and GitHub without knowing Git commandline commands.

## Creating your GitHub account.

1) To get started, open the GitHub.com page, where you enter your email in the middle of the homepage and click the green "Sign up for GitHub" button.
2) After that, you’ll go to a new page where you confirm your email and create a password.
3) Then, you’ll receive an email from GitHub with a launch code. Open GitHub using the green button in the email and enter the code to verify your account.
4) Once that’s done, you’ll have a GitHub account and can start creating and accessing "Repositories."

Additional setup information

1) To create a "Repository," often just called a "Repo".
2) There is a dropdown menu on the left side of the screen in your GitHub area where you can click the green button that says "New."
3) There, you name the Repo and choose whether you want to include a .gitignore, README, and other options.
4) To add collaborators to the Repo, start by going to the homepage of the Repo by clicking on it.
5) Then go to "Settings" at the top, under the name of the Repo.
6) In the "Settings" tab of the Repo, at the top under "Access," there is a section called "Collaborators," which you click.
7) On the screen, under "Manage Access," there is a green button that says "Add People." Click it and type the GitHub username of the person you want to invite to the Repo.
8) That person will then receive an email in the inbox linked to their GitHub account where they can accept the invitation.

## "Cloning", "Commits", "Push", "Pull"

The following assumes that you have already downloaded and setup Github Deskop on your Local computer that you will be working on.

- Cloning
  1) Once you have either created or joined a GitHub repo you will need to clone it to you local computer to share code/documentation with your group members.
  2) To Clone the GitHub repo onto your local computer, the simplest way using GitHub Desktop is to open GitHub Desktop, then open the main repo screen, which is under the "<> Code" in the top right side of the screen under the repo's name.
  3) On that screen you will see the branch you are looking at, the documents in that branch and then a large green button called "<> Code".
  4) Press that button and a dropdown will appear, the default screen is under "HTTPS" and from there you will press the button in the middle called "Open with GitHub Desktop".
  5) This will prompt you to clone that repository in the GitHub Desktop application, after you accept cloning you can share files.

- Pulling
  1) Assuming you have already cloned the repository, you now are able to pull new files that have been pushed to the GitHub repo onto your local computer for you to work on in your own IDE.
  2) Before you start implementing something, it is recommended that you check if there are any new commits to the GitHub repository to avoid conflicts later down the line.
  3) To pull changes in GitHub Desktop, you first check your "Current Repository" and make sure that its the correct one, then you check if your "Current Branch" is the correct one.
  4) After verifying the repo and branch you then press "Fetch Origin" and you can see the changes that have been made, after that you press the blue button on the top right of the screen called "Pull Origin".
  5) This will sync your local copy with the latest changes from the GitHub repo.

- Commits
  1) After making changes to files in your local copy of the repository, you will need to commit those changes in GitHub Desktop.
  2) To commit, open GitHub Desktop, and select the repository and branch where your changes are made.
  3) In the "Changes" tab, you will see a list of modified files. Add a commit message describing what changes you made in the box on the bottom left, you need a summary and then an optional more detailed description.
  4) Once you've written your message, click the "Commit to main" button (or the appropriate branch name) to save those changes locally.
  5) This saves your work on your computer but doesn't share it with others in the repo yet.

- Pushing
  1) After committing your changes locally, you will need to push them to the GitHub repository so that your group members can see them.
  2) To push your changes, go to GitHub Desktop, and with the correct repository and branch selected, click the blue "Push Origin" in the top right of the screen.
  3) This uploads your local commits to the GitHub server, making them available to others working on the same repository.
  4) Now your changes are live on GitHub, and others can pull them to update their own local copies.

## "Pull Requests" and "Code Reviews"

- Pull Request
  1) After pushing your changes to GitHub, if you're working on a different branch and want to merge your changes into the main branch, you need to create a Pull Request (PR).
  2) To create a Pull Request, go to the GitHub website and navigate to the correct repository home screen.
  3) On the repository page, click the "Pull Requests" tab located on the border below the repository name and then click the green "New Pull Request" button.
  4) Select the branch you want to merge from (The branch you have been working on) and the branch you want to merge into (usually the main branch).
  5) You then compare the branches and click "Create Pull Request".
  6) Add a title and description, explaining the changes you've made.
  7) Click "Create Pull Request" again now on the bottom right to submit it. Now others can review and discuss your changes before they are merged.
  8) GitHub has a feature where it automatically checks if there are any conflicts if you were to merge directly without resolving anything.
  9) If there is no conflict detected you can choose to skip Code Reviews and just merge directly by clicking "Merge Pull Request", this is however not recommended since others may have changed something.
     
- Code Reviews
  1) After you’ve created a Pull Request, your team members will be notified and can review your changes.
  2) Reviewers can leave comments on specific lines of code, suggest changes, or approve the changes.
  3) To leave a comment, simply click on the Pull Request and type your feedback in the comment box.
  4) If reviewers suggest changes, you can modify your code locally, commit the changes, and push them to the same branch. The Pull Request will automatically update with the new changes.
  5) Once the reviewers approve the changes, the Pull Request can be merged into the main branch.
  6) After merging, you may delete the feature branch if it is no longer needed, and everyone can pull the updated code from the main branch.

## "Branching" and "Merging"

- Branching
  1) In Git, a branch is a separate line of development allowing you to work on features without affecting the main project.
  2) To create a new branch using GitHub Desktop, open the app and select your repository.
  3) From the top bar, click on "Current Branch" and then "New Branch".
  4) Give your new branch a name (TestBranch..) and click "Create Branch". Now all changes you make and commit, pushes and pulls are on that branch.
  5) Any changes you make will be kept isolated in this branch, allowing you to work on new features or fixes without affecting the main branch or other branches people may be working on.
  6) You can switch between branches at anytime by clicking on "Current Branch" and selecting the one you want.

- Merging
  1) After finishing the work you created the branch to do, you'll need to merge it into the main branch to include your changes in the project.
  2) To merge a branch in GitHub Desktop, first, make sure you’re on the branch you want to merge into (usually main).
  3) Then, click on the "Branch" menu at the top and select "Merge into Current Branch".
  4) Choose the branch you want to merge from (TestBranch..), and click "Merge".
  5) Git will attempt to merge the changes automatically. If there are no conflicts, the changes will be merged.
  6) If there are conflicts, Git will notify you and ask you to resolve them manually before completing the merge.
  7) Once merged, you can delete the branch if it’s no longer needed and push the changes to the GitHub repository to update everyone else’s copy.
  8) Another way to do this is by creating a Pull Request as mentioned before.


## "Branching Strategies"

- Git flow

  The main idea behind the Git flow branching strategy is to isolate your work into different types of branches. There are five different branch types in total:

  1) Main
  2) Develop
  3) Feature
  4) Release
  5) Hotfix
  
  The two primary branches in Git flow are main and develop. There are three types of supporting branches with different intended purposes: feature, release, and hotfix.

  The Git flow branching strategy comes with many benefits, but does introduce a few challenges.

  - The Benefits of Git Flow:

    1) The various types of branches make it easy and intuitive to organize your work.
    2) The systematic development process allows for efficient testing.
    3) The use of release branches allows you to easily and continuously support multiple versions of production code.

  - The Challenges of Git Flow:

    1) Depending on the complexity of the product, the Git flow model could overcomplicate and slow the development process and release cycle.
    2) Because of the long development cycle, Git flow is historically not able to support Continuous Delivery or Continuous Integration.

Source (https://www.gitkraken.com/learn/git/best-practices/git-branch-strategy)

- Feature Branching

  Feature Branching is a commonly used workflow that involves creating a new branch for a specific feature or change in the codebase. This allows developers to work on the feature independently without affecting the main branch. When the feature is complete, it can be merged back into the main branch through a pull request. The pull request allows other team members to review the changes and suggest modifications or improvements before merging the feature into the main branch.

  - Feature Branching Workflow
    
    1) Create feature branches: Create a new branch for each feature or task you're working on. This branch should be created from the main branch.
    2) Work on the feature: After creating the feature branch, you can start implementing the new feature by making as many commits as necessary. The branch should only contain changes relating to that particular feature.
    3) Create a pull request: When you're finished working on the feature branch, you create a pull request to merge the changes into the main branch.
    4) Review and approve: Other developers review the changes in the pull request and approve them if they are satisfied with the changes. Code review can help catch issues or mistakes before they are merged into the main branch.
    5) Merge the feature branch: Once you're done working on the feature, you can merge the feature branch back into the main branch.
    6) Clean up: After merging, you can delete the feature branch, as it is no longer needed.

Source (https://tilburgsciencehub.com/topics/automation/version-control/advanced-git/git-branching-strategies/)

- Trunk Based Development
  Trunk Based Development promotes a single shared branch called “trunk” and eliminates long-living branches. There are two variations based on team size: smaller teams commit directly to the trunk, while larger teams create short-lived feature branches. Frequent integration of smaller feature slices is encouraged to ensure regular merging.
  
  Pros:
  - Encourages DevOps and unit testing best practices.
  - Enhances collaboration and reduces merge conflicts.
  - Allows for quick releases.
  
  Cons:
  - Requires an experienced team that can slice features appropriately for regular integration.
  - Relies on strong CI/CD practices to maintain stability.

Source (https://medium.com/@sreekanth.thummala/choosing-the-right-git-branching-strategy-a-comparative-analysis-f5e635443423)

## Resolving conflicts.

When multiple developers are working on the same project, conflicts can occur when changes are made to the same part of a file in different branches or commits. Git cannot automatically decide which change should take precedence, so it flags these situations as conflicts that need to be resolved manually.

A common conflict occurs when you create a new branch off main and start developing on that branch, sometime after that another group member pushes his changes that he made to a file to main, you finish developing and want to merge your branch back into main but now the file he changed has two different versions, the one you have without the new additions and the one the other group memeber made. Essentially to solve this "conflict", you will need to decide which version of that file you want to use when you push your changes to main.

- A general plan to resolve conflicts
  1) After getting a conflict message when pushing to or pulling from a branch you need to open the file in your IDE.
  2) One part of that file represents the changes you made and the other represents the changes another group member made.
  3) You need to figure out whether you want to either discard one for the other or combine them into one.
  4) Once you've either combined the changes or discarded one you can commit and push that resolved filed onto the branch.

- Some best practices to avoid conflicts
  1) Communcation within the team, make sure that whenever you push a change to the GitHub Repository that you communicate that to your team, a simple "Hey i just pushed "X" to the Repo" is enough for the other group members to know that they may need to pull changes.
  2) Before you start working on implementing something, check if anyone has pushed something new to the repo for you to pull. In addition to this you should check the git status frequently.
  3) Breaking off into branches, pushing frequently by breaking your changes into smaller more manageable pieces can avoid conflicts or minimize the likelihood of them happening.

## Common issues and resolutions to them

Some common issues and how to resolve them using GitHub Desktop.

- Merge conflicts are the most common issues
  1) GitHub Desktop will show you that there is a conflict in the file by displaying a "Conflicted" status on the file.
  2) Click on the conflicted file. GitHub Desktop will show you a button to open the file in your IDE.
  3) Open the file and manually resolve the conflict by choosing which version of the changes to keep (yours, theirs, or a combination).
  4) Once resolved, save the file and return to GitHub Desktop.
  5) Click "Mark as Resolved" for the file in GitHub Desktop.
  6) Commit the resolution with a message like "Resolved merge conflict".
 
- Push Rejected
  1) This happens when your local branch is behind the remote branch so GitHub rejects your push.
  2) You can resolve this in GitHub Desktop by navigating into the Repository and branch and pulling the latest changes from the remote branch into your local one.
  3) This may cause some merge conflicts if you have made changes on your local branch which will need to be resolved.
  4) You can then proceed with the normal commits and push methods.

- Merge Conflict not resolved properly and files were overwritten
  1) This is when you accidentally overwrite files in the remote repository when resolving a merge conflict and pushing local changes to remote.
  2) GitHub keeps track of older versions of the repository so you can either go into a previous version and fetch the overwritten files.
  3) Or in GitHub Desktop click on History and right click on the commit you made overwriting the file and press "Revert changes in commit".
  4) This reversion will create a new commit which you need to push to revert to the older one.

 - Git Repository/Branch not found
  1) This can happen if a repository/branch is deleted or moved, may also appear if you change your local directories.
  2) First verify that the repository/branch still exists on GitHub.
  3) Check your local directory.
  4) Assuming that the GitHub repository still exists the simplest way to resolve this is to clone the repository again.
  5) If a branch has been deleted you can either fetch it from History or create it again.
     
