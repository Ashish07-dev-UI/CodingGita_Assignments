// Create a nested switch program:
// First take a role (“admin” or “user”).
// If role is “admin”, then take an action (“create”, “edit”, “delete”) and print the corresponding message.
// If role is “user”, print “Limited Access”.





let role = "admin";
let action = "create";

switch (role) {
    case "admin":
        switch (action) {
            case "create":
                console.log("Create permission granted");
                break;

            case "edit":
                console.log("Edit permission granted");
                break;

            case "delete":
                console.log("Delete permission granted");
                break;

            default:
                console.log("Invalid action");
                break;
        }
        break;

    case "user":
        console.log("Limited Access");
        break;

    default:
        console.log("Invalid role");
        break;
}