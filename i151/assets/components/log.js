AFRAME.registerComponent("log", {
  schema: {
    message: { type: "string", default: "message" },
  },

  init: function () {
    var strLog = this.data.message;
    console.log(strLog);
  },
});
