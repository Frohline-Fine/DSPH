import QtQuick.Layouts

Window {
    width: 800
    height: 600

    ColumnLayout {
        anchors.fill: parent
        spacing: 10

        Rectangle {
            color: "azure"
            Layout.preferredWidth: 100
            Layout.preferredHeight: 150
        }

        Rectangle {
            color: "plum"
            Layout.fillWidth: true
            Layout.fillHeight: true
        }
    }
}