AFRAME.registerComponent("cursor-listener",{

    schema:{
        selectedItemId: {type: "string", defaut:""},
    },

    init: function(){
        this.handlerMouseEnterEvents();
        this.handlerMouseLeaveEvents();
    },
 
    handlerMouseEnterEvents: function () {
        this.el.addEventListener("mouseenter", () => {
            this.handlePlaceListState();
        })
    },

    handlerMouseLeaveEvents: function () {
        this.el.addEventListener("mouseleave", () => {
            const { selectedItemId } = this.data;
            if(selectedItemId) {
                const el = document.querySelector(`#${selectedItemId}`) // "#"+selectedItemId
                const id = el.getAttribute("id");
                if(id == selectedItemId) {
                    el.setAttribute("material", {
                        color:"#00bcd4",
                        opacity: 0.4,
                    });
                }
            }
            
        })
    },

    handlePlaceListState: function(){
        const id = this.el.getAttribute("id");
        const placesId = ["taj-mahal", "budapest", "new-york", "eiffel-tower"]
        if (placesId.includes(id)){
            const placesContainer = document.querySelector("#places-container");
            placesContainer.setAttribute("cursor-listener",{
                selectedItemId:id,
            });
            this.el.setAttribute("material", {
                color: "#D76b30",
                opacity: 1,
            })
        }
    },
});